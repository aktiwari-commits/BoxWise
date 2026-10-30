# Chat Transcript Summary

## Prompt 1

I received a Python/Django hiring assignment to build an AI-Assisted Box Selection System and asked for guidance on how to approach it.

### AI Assistance

- Explained the assignment requirements.
- Broke the project into manageable steps.
- Suggested creating separate apps for:
  - Products
  - Boxes
  - Orders
  - Recommendations

---

## Prompt 2

I asked for a complete implementation roadmap because I had only 24 hours to finish the assignment.

### AI Assistance

Suggested:

- Django project structure
- Database design
- API design
- Recommendation service layer
- Unit testing strategy
- README structure
- AI_USAGE.md structure

---

## Prompt 3

I requested detailed explanations of Django concepts rather than only code.

### AI Assistance

Explained:

- Django Projects
- Django Apps
- Models
- Migrations
- ORM
- Serializers
- Views
- URLs
- Testing
- Service Layer Architecture

---

## Prompt 4

I requested help designing the application architecture.

### AI Assistance

Suggested implementing:

### Product Model

Attributes:

- Name
- Length
- Width
- Height
- Weight

### Box Model

Attributes:

- Name
- Length
- Width
- Height
- Maximum Weight Capacity
- Cost

### Order Model

Attributes:

- Products
- Created Timestamp

---

## Prompt 5

I requested help implementing the recommendation algorithm.

### AI Assistance

Suggested algorithm:

1. Retrieve products from order.
2. Calculate total order weight.
3. Retrieve available boxes.
4. Validate weight constraints.
5. Validate dimension constraints.
6. Collect valid boxes.
7. Select the lowest-cost valid box.
8. Return recommendation.

---

## Prompt 6

I requested guidance for testing.

### AI Assistance

Suggested test scenarios:

- Valid recommendation
- Cheapest box selection
- Weight limit validation
- Dimension validation
- Oversized product handling
- No suitable box available
- Empty order handling

---

## Prompt 7

I requested help creating project documentation.

### AI Assistance

Helped create:

- README.md
- AI_USAGE.md
- Submission checklist
- Project explanation

---

## Verification Performed

The final implementation was verified using:

- Django migrations
- Application testing
- Unit tests
- Manual validation of recommendation logic
- Documentation review

---

## Note

AI assistance was used for learning, design guidance, architecture suggestions, documentation support, and code review. Final implementation decisions, project structure setup, testing execution, debugging, and submission preparation were performed by the developer.
