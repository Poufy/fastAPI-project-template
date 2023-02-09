## Notes

### Why do we use dependency injection to pass the db object to the controller?

When using the Depends keyword in a FastAPI application, you are using dependency injection. Dependency injection is a software design pattern that allows for the removal of hard-coded dependencies and makes it possible to change them, whether at run-time or compile-time.

By initializing the database session in the router and passing it to the controller using the Depends keyword, you are decoupling the database logic from the controller logic. This allows you to change the database implementation without having to change the code in the controller, as long as the interface remains the same. This can make your code more flexible and easier to maintain, as you can swap out components with minimal impact on the rest of your code.

Additionally, by using the Depends keyword, FastAPI will take care of creating and disposing of the database session for you. This means that you don't have to worry about managing the lifetime of the database session, which can be a complex task, especially in a high-performance web application.

In summary, using dependency injection with the Depends keyword in FastAPI helps to decouple the database logic from the controller logic, making your code more flexible and easier to maintain, and allowing FastAPI to manage the lifetime of the database session for you.