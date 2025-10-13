@st.cache_data
def foo(bar):
    # Do something expensive and return data
    return data

# Executes foo
d1 = foo(ref1)

# Does not execute foo
# Returns cached item by value, d1 == d2
d2 = foo(ref1)

# Different arg, so function foo executes
d3 = foo(ref2)

# Clear the cached value for foo(ref1)
foo.clear(ref1)

# Clear all cached entries for this function
foo.clear()

# Clear values from *all* in-memory or on-disk cached functions
st.cache_data.clear()
