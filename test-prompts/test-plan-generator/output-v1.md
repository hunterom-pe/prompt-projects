# QA Test Plan – User Login Feature

---

## 1. Introduction

This document outlines the test plan for the User Login feature of the web application. The goal is to ensure secure, reliable, and user-friendly access to the platform via email and password.

---

## 2. Objectives

- Verify functional requirements of the login system
- Validate input field behavior (email and password)
- Confirm proper error handling and validation
- Test across multiple browsers and devices
- Check for security vulnerabilities (e.g., SQL injection)

---

## 3. Scope

### In Scope:
- Email/password login functionality
- “Forgot password” link
- Error messages
- UI validation and rendering
- Basic security checks (e.g., character limits, input sanitation)

### Out of Scope:
- OAuth or SSO login
- Signup/registration functionality

---

## 4. Test Strategy

- **Black-box testing**
- **Exploratory testing**
- **Cross-browser testing**
- **Regression testing**
- **UAT on staging**

---

## 5. Tools

- TestRail (Test Case Management)
- Jira (Bug Tracking)
- Postman (API Validation)
- BrowserStack (Cross-browser testing)

---

## 6. Environment

- Staging Environment URL: `staging.example.com/login`
- Browser Versions: Chrome 114+, Firefox 102+, Safari (iOS 16+), Edge
- Devices: Desktop (macOS + Windows), iPhone, Android

---

## 7. Test Data

- Valid users:
  - testuser1@example.com / Password123!
  - qauser2@example.com / SecurePass456!
- Invalid users:
  - wrongemail@example.com / WrongPass
  - blank fields

---

## 8. Test Cases (Overview)

| ID     | Title                      | Type        | Priority | Notes                        |
|--------|----------------------------|-------------|----------|------------------------------|
| TC001  | Successful login           | Functional  | High     | With valid email/password    |
| TC002  | Invalid password           | Negative    | High     | Valid email, wrong password  |
| TC003  | Blank fields               | Validation  | Medium   | Form submitted empty         |
| TC004  | SQL Injection attempt      | Security    | High     | Ensure input sanitation      |

(Full test cases will be included in a separate attachment)

---

## 9. Risks & Mitigations

| Risk                                  | Mitigation                             |
|---------------------------------------|----------------------------------------|
| Outages during login                  | Deploy after-hours with rollback plan  |
| Missing edge-case validation          | Extensive exploratory test coverage    |
| Browser-specific UI issues            | Use BrowserStack, manual QA on iOS     |

---

## 10. Timeline

| Phase               | Dates                 |
|---------------------|------------------------|
| Test Case Creation  | July 29 – July 30      |
| Test Execution      | July 31 – Aug 2        |
| Bug Fix & Re-test   | Aug 3 – Aug 4          |
| Final Approval      | Aug 5                  |

---

## 11. Approvals

- QA Lead: Hunter Ortega-Mathews
- Product Owner: [Insert Name]
- Dev Lead: [Insert Name]
