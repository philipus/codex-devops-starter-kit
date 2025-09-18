# US001 - File Upload with Validation

## Title
As a user, I want to upload files with size/type validation so that only allowed content enters the system.

## Description
Create an API endpoint to upload files with checks:
- Only PDF, CSV, TXT allowed
- Max size: 5MB
- Error messages for invalid input

## Tasks
- [ ] Define route `/upload`
- [ ] Add validation logic in `services/`
- [ ] Create `ValidationError` exception
- [ ] Add error handlers
- [ ] Unit test for two scenarios (valid/invalid)

## Acceptance Criteria
- [ ] Upload succeeds with valid file
- [ ] Upload fails with invalid type
- [ ] Upload fails with file too large
- [ ] All tests pass (`pytest`)
