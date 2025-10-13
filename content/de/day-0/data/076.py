@st.cache_resource
def foo(bar):
    # Create and return a non-data object
    return session

# Executes foo
s1 = foo(ref1)

# Does not execute foo
# Returns cached item by reference, s1 == s2
s2 = foo(ref1)

# Different arg, so function foo executes
s3 = foo(ref2)

# Clear the cached value for foo(ref1)
foo.clear(ref1)

# Clear all cached entries for this function
foo.clear()

# Clear all global resources from cache
st.cache_resource.clear()
