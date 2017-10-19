
## Table of Contents
* [Viewing the Response Body](#response-body)

<a name="response-body"></a>
## Viewing the Response Body

When debugging or testing, it may be useful to examine the raw request body.

You can do this just after call `response = client.your.api._(param).call.<METHOD>` Where <METHOD> can be `get()`, `post()`, `patch()` and `post()`.

```python
print(response.body)
```
