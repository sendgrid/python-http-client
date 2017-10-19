
## Table of Contents
* [Viewing the Request Body](#request-body)


<a name="request-body"></a>
## Viewing the Request Body

When debugging or testing, it may be useful to examine the raw request body.

You can do this just after call `response = client.your.api._(param).call.<METHOD>` Methods can be `get()`, `post()`, `patch()` and `post()`.
After the call you just need to do as follow:

```python
print response.body
```
