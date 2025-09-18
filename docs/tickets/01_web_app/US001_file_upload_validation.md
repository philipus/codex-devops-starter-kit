# US001 - File Upload with Validation

## Title
As a user, I want to upload files with size/type validation so that only allowed content enters the system.

## Description
Create an API endpoint to upload files with checks:
- Only PDF, CSV, or TXT allowed
- Max size: 5MB
- Error messages for invalid input

## Tasks
- [x] Define route `/upload`
- [x] Add validation logic in `services/`
- [x] Create `ValidationError` exception
- [x] Add error handlers
- [x] Unit test for valid and invalid scenarios

## Acceptance Criteria
- [x] Upload succeeds with valid `.csv`, `.txt`, or `.pdf`
- [x] Upload fails with unsupported file type
- [x] Upload fails with file too large
- [ ] All tests pass (`pytest`)
