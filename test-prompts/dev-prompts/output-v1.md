# AI Output

**Summary:**

This function takes a list of user dictionaries and returns only those who are active and have logged in at least once.

**Suggestions:**

* Could use a list comprehension for cleaner code.
* Might want to sort by last_login or include logging for traceability.

**Edge Cases:**

* No check for missing keys like 'is_active' or 'last_login'.
* Could fail silently if user dicts are malformed.

**Test Suggestions:**

* Test with missing keys
* Test with all users inactive
* Test with mix of active and inactive users