# **asyncio**

asyncio is Python’s built-in library for writing asynchronous, non-blocking code.
It is designed for efficient waiting, not parallel execution.

## Core Idea of Asyncio

    -Only one piece of code runs at a time

    -Code pauses voluntarily when waiting

    -The event loop switches between tasks

    -No threads are required

    -This model is called cooperative multitasking.

# Event Loop

What Is the Event Loop?

        -The event loop is the heart of asyncio.

        -It runs continuously

        -Schedules and executes tasks

        -Monitors I/O operations

        -Decides when coroutines run or pause

## Responsibilities

        -Run coroutines

        -Resume paused coroutines

        -Handle timers and I/O events

        -Manage Futures and Tasks
        -Running asynchronous code

        -Deciding what runs next

        -Pausing and resuming tasks

        -Handling I/O events (network, sleep, timers)

## What It Actually Does

    -Internally, the event loop:

        -Keeps a list of tasks

        -Runs a task until it reaches await

        -Pauses that task

        -Runs another ready task

        -Resumes paused tasks when their I/O completes

# 2. Coroutines

What They Are

A coroutine is a function defined using async def.
Calling it does not execute it:

async def read_data():
...
coro = read_data()

This creates a coroutine object, not a result.

Why Coroutines Can Pause

Coroutines contain await points.
await some_io()

### At await:

The coroutine pauses

Control goes back to the event loop

Another task can run

This is how concurrency happens.

# Futures

What a Future Is

A Future is an object that:

Represents a value that will exist later

Starts in a pending state

Eventually holds a result or an exception

Think of it as:

“I will have a result, but not yet.”

# Who Creates Futures

Mostly created by the event loop

Used internally by tasks and I/O operations

Rarely created manually by application code

# What a Task Is

A Task is:

A coroutine that has been scheduled

Wrapped inside a Future

Managed by the event loop

task = asyncio.create_task(read_data())

The coroutine is registered with the loop

Execution starts automatically

The task can pause and resume

# Why Tasks Matter

Without a Task:

Coroutines never run

They just exist as objects

Tasks are what make coroutines active.

# Execution Flow (Step by Step)

Event loop starts

Task is created

Task starts running its coroutine

Coroutine reaches await

Task pauses

Event loop runs another task

I/O completes

Task resumes

Only one task runs at a time, but none are blocked.

## Why This Design Exists

This design allows:

Thousands of I/O operations

With minimal overhead

Using a single thread

It avoids:

Thread creation cost

Locks

Context switching

## Simple Mental Model

Event Loop → Manager

Coroutine → Pausable job

Future → Promise of a result

Task → Scheduled job
