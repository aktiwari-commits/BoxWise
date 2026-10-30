from itertools import permutations, product as cartesian_product


def get_orientations(dimensions):
    """
    Generate all possible orientations of a product.
    """

    return set(permutations(dimensions))


def has_overlap(position1, position2):
    """
    Check whether two placed products overlap.
    """

    x1, y1, z1, l1, w1, h1 = position1
    x2, y2, z2, l2, w2, h2 = position2

    separated = (
        x1 + l1 <= x2 or x2 + l2 <= x1 or
        y1 + w1 <= y2 or y2 + w2 <= y1 or
        z1 + h1 <= z2 or z2 + h2 <= z1
    )

    return not separated


def get_candidate_positions(placed_items):
    """
    Generate possible positions for the next product.
    """

    x_values = {0}
    y_values = {0}
    z_values = {0}

    for item in placed_items:

        x, y, z, length, width, height = item

        x_values.add(x + length)
        y_values.add(y + width)
        z_values.add(z + height)

    positions = cartesian_product(
        sorted(x_values),
        sorted(y_values),
        sorted(z_values)
    )

    return sorted(
        positions,
        key=lambda point: (point[2], point[1], point[0])
    )


def pack_products(box, products):
    """
    Attempt to pack all products inside one shipping box.
    """

    box_length = box.length
    box_width = box.width
    box_height = box.height

    # Expand quantities into individual physical products.
    items = []

    for product_item in products:

        product = product_item.product

        dimensions = (
            product.length,
            product.width,
            product.height
        )

        for _ in range(product_item.quantity):
            items.append(dimensions)

    # Try larger products first.
    items.sort(
        key=lambda dimensions:
        dimensions[0] * dimensions[1] * dimensions[2],
        reverse=True
    )

    placed_items = []

    for dimensions in items:

        product_placed = False

        orientations = get_orientations(dimensions)

        positions = get_candidate_positions(placed_items)

        for orientation in orientations:

            length, width, height = orientation

            # Check box boundaries.
            if (
                length > box_length or
                width > box_width or
                height > box_height
            ):
                continue

            for x, y, z in positions:

                # Check whether product stays inside the box.
                if (
                    x + length > box_length or
                    y + width > box_width or
                    z + height > box_height
                ):
                    continue

                new_item = (
                    x, y, z,
                    length, width, height
                )

                # Check collisions with existing products.
                overlap = any(
                    has_overlap(new_item, existing)
                    for existing in placed_items
                )

                if not overlap:

                    placed_items.append(new_item)

                    product_placed = True

                    break

            if product_placed:
                break

        if not product_placed:
            return False

    return True


def recommend_box(order):
    """
    Recommend the cheapest feasible shipping box.
    """

    products = list(
        order.items.select_related("product")
    )

    if not products:
        raise ValueError("Order has no products.")

    total_weight = sum(
        item.product.weight * item.quantity
        for item in products
    )

    from boxes.models import Box

    available_boxes = Box.objects.all().order_by("cost")

    results = []

    for box in available_boxes:

        # First check weight capacity.
        if total_weight > box.max_weight:

            results.append({
                "box": box,
                "feasible": False,
                "reason": "Maximum weight capacity exceeded."
            })

            continue

        # Then check physical packing.
        fits = pack_products(box, products)

        if fits:

            results.append({
                "box": box,
                "feasible": True,
                "reason": "All products fit within the box."
            })

        else:

            results.append({
                "box": box,
                "feasible": False,
                "reason": "Products cannot be packed using the current algorithm."
            })

    suitable_boxes = [
        result for result in results
        if result["feasible"]
    ]

    suitable_boxes.sort(
        key=lambda result: result["box"].cost
    )

    recommended = (
        suitable_boxes[0] if suitable_boxes else None
    )

    return {
        "order": order,
        "total_weight": total_weight,
        "recommended": recommended,
        "all_results": results
    }