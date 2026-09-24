# Reflection

## What did you ask Copilot to help you build? How did you break down the problem?

I asked Copilot to help me build a basic entertainment platform, similar to YouTube or
Spotify, with content display and a basic player, using a Python + Flask backend. Rather
than asking for the whole app at once, I broke the problem into stages:

1. First I just stated the goal and tech stack, without asking for any code yet, so
   Copilot understood the scope before touching files.
2. I let Copilot propose concrete decisions (content type, storage, frontend approach)
   instead of specifying everything myself,I used what Copilot suggested, reviewed it, then confirmed with "keep it simple and
   decide for me" along with a couple other structure ideas.
3. I asked for the basic project structure (models, routes, templates, static assets)
   as one step.
4. I then asked Copilot to focus on just one or two files at a time (`models.py` and
   `app.py`) rather than regenerating the whole project, which kept changes reviewable.
5. Once the core files were solid, I asked it to move forward incrementally (fixing the
   templates to match the model changes, adding a `.gitignore`, and adding category
   filtering) instead of doing everything in one shot.
6. Finally, I asked it to run the app and verify the routes actually worked instead of
   just trusting the code looked correct.

## How did your approach to asking questions change as you worked?

Early on, my prompts were broad ("recreate a basic version of an entertainment
platform"). As the project took shape, my prompts became more targeted and incremental —
I asked for specific files, specific features (category filters), and specific
verification steps (curl checks, running the server) rather than open-ended requests.
I also shifted from asking Copilot to just write code to asking it to run and verify
its own output, which caught a real bug (local video/thumbnail file paths that didn't
exist) before it became a bigger problem.

## What parts of the development process with GitHub Copilot surprised you?

I was surprised that Copilot didn't just generate code — it actually ran the Flask
server, curled the routes, checked HTTP status codes, and used that evidence to confirm
things worked, rather than assuming. When the app wasn't reachable in the browser, it
methodically diagnosed the issue (checked `ss -ltnp`, confirmed the process was
listening, tried `host="0.0.0.0"`, then suggested changing ports when there was likely a
host-side conflict) instead of guessing at fixes blindly.

## What did you learn about the technology you used that you didn't know before?

I learned that a Flask dev server bound to `127.0.0.1` is invisible to port-forwarding
tools like the VS Code/Codespaces "Ports" panel — it has to be bound to `0.0.0.0` to be
reachable from outside the container. I also learned that common default ports (like
5000) can silently conflict with other services (e.g., AirPlay Receiver on macOS),
which is why switching to an alternate port (8000) resolved the forwarding issue.

## What would you do differently if you had to build this again?

I would decide on the port and host-binding configuration (`0.0.0.0`, non-default port)
up front, since that caused most of the friction at the end of the project. I'd also
seed the database with real hosted sample media from the start instead of first
scaffolding local file paths that didn't exist yet — that would have avoided an
unnecessary rework step in `models.py`/`app.py`/templates.
