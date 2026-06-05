# 🎉 Evently API - Complete Project Documentation

A Flask-based REST API for managing events and RSVPs with role-based access control. This educational project demonstrates REST API design, JWT authentication, database modeling, and comprehensive testing practices.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Tests](https://img.shields.io/badge/Tests-13%20Passing-brightgreen.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Live Resources & Production Links

### ✨ Your Live Application

| Resource | Link | Status |
|----------|------|--------|
| 🌐 **Production API** | [events-api-latest-rsgk.onrender.com](https://events-api-latest-rsgk.onrender.com) | ✅ Live on Render |
| 🐳 **Docker Image Repository** | [hub.docker.com/r/abhisakh/events-api](https://hub.docker.com/r/abhisakh/events-api) | ✅ Hosted on Docker Hub |
| 💻 **GitHub Repository** | [github.com/abhisakh/events-api](https://github.com/abhisakh/events-api) | ✅ Source Code & CI/CD |

### Quick Links to Test Your API

#### Command Line Testing
```bash
# Health Check (Verify API is running)
curl https://events-api-latest-rsgk.onrender.com/api/health

# Get All Events
curl https://events-api-latest-rsgk.onrender.com/api/events

# View OpenAPI Specification (JSON format)
https://events-api-latest-rsgk.onrender.com/api/openapi.yaml
```

#### 🎯 Interactive Testing with Swagger UI

**Access Swagger UI in Production:**
```
👉 https://events-api-latest-rsgk.onrender.com/apidocs
```

**Steps to Test API Endpoints:**

1. **Open the URL above** in your browser
   - You'll see the Swagger UI interface with all available endpoints
   - All 17 endpoints documented and testable

2. **Select the Production Server** ⚠️ **IMPORTANT!**
   - Look for the **"Servers"** dropdown in the top-right of Swagger UI
   - You'll see two options:
     ```yaml
     • http://localhost:4000
     • https://events-api-latest-rsgk.onrender.com  ← SELECT THIS ONE
     ```
   - **Click and select**: `https://events-api-latest-rsgk.onrender.com`
   - This routes all your test requests to the live production API

3. **Start Testing Endpoints**
   - Click any endpoint to expand it
   - Click "Try it out" button
   - Fill in parameters (if needed)
   - Click "Execute" to make the request
   - See response in real-time

**Example Test Flow:**
```
1. Open https://events-api-latest-rsgk.onrender.com/apidocs
2. Select Server: "https://events-api-latest-rsgk.onrender.com"
3. Click "GET /api/events"
4. Click "Try it out"
5. Click "Execute"
6. See all events in production! ✅
```

**Available Test Endpoints:**

| Endpoint | Method | Purpose | Auth Required |
|----------|--------|---------|---|
| `/api/health` | GET | Check API health | No |
| `/api/events` | GET | List all events | No |
| `/api/events/{id}` | GET | Get event details | No |
| `/api/auth/register` | POST | Register new user | No |
| `/api/auth/login` | POST | Login & get JWT token | No |
| `/api/events` | POST | Create new event | **Yes** |
| `/api/rsvps/event/{id}` | POST | RSVP to event | Depends on event |
| `/api/rsvps/event/{id}` | GET | View RSVPs for event | No |

**Quick Test Suggestions:**
1. ✅ Test health check first (GET /api/health)
2. ✅ List all events (GET /api/events)
3. ✅ Register a new user (POST /api/auth/register)
4. ✅ Login with your credentials (POST /api/auth/login)
5. ✅ Create a new event (POST /api/events) - Use JWT token from step 4
6. ✅ RSVP to an event (POST /api/rsvps/event/{id})
7. ✅ View RSVPs (GET /api/rsvps/event/{id})

---

### Production Dashboard Links

| Tool | Purpose | Access |
|------|---------|--------|
| 🔷 **Render Dashboard** | Monitor deployment, view logs, manage service | [dashboard.render.com](https://dashboard.render.com) → events-api-latest-rsgk |
| 🐳 **Docker Hub Dashboard** | View image tags, pull instructions, image stats | [hub.docker.com/r/abhisakh/events-api](https://hub.docker.com/r/abhisakh/events-api) |
| 🔄 **GitHub Actions Pipeline** | Monitor CI/CD pipeline, view workflow runs | [github.com/abhisakh/events-api/actions](https://github.com/abhisakh/events-api/actions) |
| 📝 **GitHub Repository** | Source code, issues, commits, branches | [github.com/abhisakh/events-api](https://github.com/abhisakh/events-api) |

---

## 📋 Comprehensive Table of Contents

### 🚀 Quick Start & Production Links
- [Live Resources & Production Links](#-live-resources--production-links)
  - Your Live Application (Render, Docker Hub, GitHub)
  - Quick Links to Test Your API (Swagger UI, curl commands)
  - Production Dashboard Links

---

### 📁 Project Structure & Files

**1. [Project Structure](#-project-structure)**
   - Complete directory tree with file descriptions
   - Root level files (Dockerfile, docker-compose.yml, app.py, etc.)
   - File Responsibilities table (10 files documented)

**2. [File Descriptions & Responsibilities](#file-responsibilities)**
   - App.py - Flask application factory
   - Config.py - Configuration settings
   - Models.py - SQLAlchemy models (User, Event, RSVP)
   - Routes (auth.py, events.py, rsvps.py)
   - Tests (conftest.py, test_models.py, test_api.py)
   - GitHub Workflows (ci.yml)

**3. [Docker Architecture Compatibility](#-docker-architecture-compatibility)**
   - Platform specification (linux/amd64)
   - Mac vs Linux compatibility
   - Render hosting requirements
   - Architecture verification commands
   - Common issues & solutions

---

### 🚀 Development Setup & Local Deployment

**4. [Getting Started](#-getting-started)**
   - Installation instructions
   - Virtual environment setup
   - Database initialization
   - Running the application locally
   - Accessing local API & Swagger UI

**5. [Docker Setup & Usage Guide](#-docker-setup--usage-guide)**
   - 1. Local Setup and Build (docker compose up)
   - 2. Pushing to Docker Hub (docker push)
   - 3. Pulling and Running from Registry
   - 4. Testing the Docker Container
   - 5. Management Tips (stop, cleanup, inspect)

**6. [Docker Configuration](#️-docker-configuration)**
   - Dockerfile details (Python 3.11-slim, ports, environment)
   - docker-compose.yml configuration
   - Platform specification explanation
   - Service setup and environment variables

**7. [Local Development](#local-development)**
   - Building and running locally
   - Accessing the API
   - Running tests with container running

---

### 💾 Database & Application Details

**8. [Database Models](#-database-models)**
   - User Model (authentication, admin roles)
   - Event Model (event management, RSVP relationships)
   - RSVP Model (attendance tracking)
   - Access Control Matrix (public/protected/admin)
   - Model relationships & cascade deletes

**9. [API Reference](#-api-reference)**
   - Auth Routes (/api/auth/register, /api/auth/login)
   - Event Routes (GET/POST /api/events, GET /api/events/{id})
   - RSVP Routes (POST/GET /api/rsvps/event/{id})
   - App Routes (/health, /apidocs, /api/openapi.yaml)
   - Error codes and status codes

**10. [OpenAPI Specification](#openapi-specification)**
   - Server configuration (local & production)
   - API documentation format
   - Schema definitions
   - Security schemes (JWT)

---

### 🧪 Testing (17 Complete Tests)

**11. [Test Configuration (conftest.py)](#-conftest.py---test-configuration--fixtures)**
   - BASE_URL configuration
   - base_url fixture (session scope)
   - unique_user_credentials fixture (timestamp generation)
   - authenticated_headers fixture (JWT token creation)

**12. [Unit Tests (test_models.py)](#-file-2-test_modelspy---unit-tests-5-tests) - 5 Tests**
   - Test 1: Password hashing verification
   - Test 2: User serialization to dictionary
   - Test 3: Event with empty RSVPs
   - Test 4: Event RSVP counting & filtering
   - Test 5: RSVP serialization

**13. [Integration Tests (test_api.py)](#-file-3-test_apipy---integration-tests-8-tests) - 12 Tests**

   **Happy Path (6 Tests)**
   - Test 6: Health endpoint check
   - Test 7: User registration
   - Test 8: User login & JWT token
   - Test 9: Event creation with authentication
   - Test 10: RSVP to public event (no auth)
   - Test 11: Get all events

   **Error Handling (6 Tests)**
   - Test 12: Duplicate username rejection
   - Test 13: Event creation without auth
   - Test 14: Protected event access control
   - Test 15: Invalid event ID (404)
   - Test 16: Missing required fields
   - Test 17: RSVP to non-existent event

**14. [Designing New Tests](#-designing-new-tests)**
   - Test naming conventions & patterns
   - Happy path vs error case testing
   - Using fixtures effectively
   - Testing checklist (10 points)
   - Example test design scenarios

---

### ⚙️ CI/CD Pipeline & Automation

**15. [CI/CD Pipeline (v5)](#️-cicd-pipeline---github-actions-workflow-version-5)**
   - Workflow Overview & Triggers
   - Complete Pipeline Architecture Diagram

   **CI Job: Build, Test, and Clean**
   - 8 detailed stages (Checkout, Docker Buildx, Build, Run, Health Check, Python Setup, Tests, Cleanup)
   - Docker caching strategy
   - Health check implementation
   - Test suite execution (17 tests)

   **CD Job: Publish, Deploy, and Smoke Test**
   - Job configuration (needs: test, environment: production)
   - Docker Hub authentication & login
   - Build and Push with 3-tag strategy (latest, SHA, branch)
   - Render webhook trigger
   - 60-second rollout wait
   - Live smoke test against production

   - Execution Timeline (5-8 minutes total)
   - Failure Scenarios & Recovery
   - Critical Improvements (v4 vs v5)

**16. [GitHub Actions Secrets Configuration](#-github-actions-secrets-configuration)**
   - 4 Required Secrets Table (DOCKERHUB_USERNAME, DOCKERHUB_TOKEN, RENDER_DEPLOY_HOOK, RENDER_BASE_URL)
   - How to Create Docker Hub PAT
   - How to Get Render Deploy Hook
   - Where to find each secret

---

### 🌐 Production Deployment & Render

**17. [Render Deployment Platform – Significance & Usage](#-render-deployment-platform--significance--usage)**
   - What is Render? (6 key features)
   - Why Render for this project? (significance table)
   - Render vs Traditional Hosting comparison
   - Service Configuration (all details)
   - Health Check Endpoint (local & production)
   - Complete 10-step Deployment Flow

   **Render Usage Guide (7 Sections)**
   - Accessing Your Service (Dashboard & live application)
   - Viewing Deployment Logs (what to look for)
   - Checking Service Status (healthy vs unhealthy)
   - Manual Deployment (3 options)
   - Environment Variables
   - Rollback to Previous Version
   - Monitoring & Alerts
   - Common Issues & Solutions (7 troubleshooting cases)

**18. [Webhook & Environment Details](#-webhook--environment-details)**
   - Render Deployment Webhook (source & how it works)
   - Port Configuration explanation
   - OpenAPI Specification configuration
   - Environment Variables in Production
   - Database initialization on startup

---

### 📋 Production Operations

**19. [Deployment Checklist](#-deployment-checklist)**
   - 8-point pre-launch verification
   - Python version check
   - Port configuration verification
   - Secrets configuration validation
   - Docker Hub accessibility
   - CI/CD pipeline testing
   - Production URL reachability

**20. [Troubleshooting & Management](#-troubleshooting--management)**
   - Docker management commands
   - Container status checking
   - Log viewing and analysis
   - Common error scenarios
   - Recovery procedures

---

### 🎯 Showcase & Resources

**21. [Showcase Your Work](#-showcase-your-work)**
   - ✨ Live Production Deployment
   - 🌐 Production API (Render)
   - 🐳 Docker Hub Repository
   - 💻 GitHub Repository & Source Code
   - 📊 Production Status Dashboard
   - 🎓 What This Project Demonstrates

---

### 📊 Key Statistics

| Metric | Count |
|--------|-------|
| **Total Lines of Documentation** | 3,738 |
| **Tests Documented** | 17 (5 unit + 12 integration) |
| **API Endpoints** | 8 major endpoints |
| **Database Models** | 3 (User, Event, RSVP) |
| **Docker Files** | 2 (Dockerfile, docker-compose.yml) |
| **CI/CD Pipeline Stages** | 15 (8 CI + 7 CD) |
| **GitHub Secrets** | 4 required |
| **Production Links** | 3 (Render, Docker Hub, GitHub) |
| **File Types Documented** | 10+ |

---

### 🔍 Quick Search Guide

**Looking for specific topics?**

- **How to set up locally?** → [Getting Started](#-getting-started)
- **How to run tests?** → [Test Configuration](#-conftest.py---test-configuration--fixtures)
- **How to deploy?** → [CI/CD Pipeline](#️-cicd-pipeline---github-actions-workflow-version-5)
- **API endpoints?** → [API Reference](#-api-reference)
- **Docker info?** → [Docker Setup](#-docker-setup--usage-guide)
- **Production issues?** → [Troubleshooting](#-troubleshooting--management)
- **Test the API?** → [Live Resources](#-live-resources--production-links)
- **Render details?** → [Render Deployment](#-render-deployment-platform--significance--usage)
- **GitHub Actions?** → [CI/CD Pipeline](#️-cicd-pipeline---github-actions-workflow-version-5)
- **Database schema?** → [Database Models](#-database-models)

---

## 📁 Project Structure

```
evently-api/
├── README.md                    # Project documentation
├── Dockerfile                   # Docker image configuration (Python 3.11-slim, linux/amd64)
├── docker-compose.yml           # Docker Compose configuration (build & run)
├── app.py                       # Flask application factory & initialization
├── config.py                    # Configuration (secrets, database, JWT settings)
├── models.py                    # SQLAlchemy models (User, Event, RSVP)
├── openapi.yaml                 # OpenAPI 3.0 specification
├── requirements.txt             # Python dependencies (Flask, SQLAlchemy, etc.)
│
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI pipeline (Build, Test, Clean)
│
├── instance/
│   └── events.db                # SQLite database (auto-created on first run)
│
├── routes/                      # API Blueprint modules (organize endpoints)
│   ├── __init__.py              # Package initializer (empty)
│   ├── auth.py                  # Authentication (POST /api/auth/register, /api/auth/login)
│   ├── events.py                # Event management (GET/POST /api/events, GET /api/events/{id})
│   └── rsvps.py                 # RSVP management (POST/GET /api/rsvps/event/{id})
│
└── tests/                       # Automated test suite (17 tests total)
    ├── __init__.py              # Package initializer (empty)
    ├── conftest.py              # Pytest configuration & shared fixtures
    ├── test_models.py           # Unit tests (5 tests) - Pure Python, no I/O
    └── test_api.py              # Integration tests (12 tests) - HTTP E2E
```

### Root Level Files

| File | Purpose | Details |
|------|---------|---------|
| `README.md` | Project documentation | Comprehensive guide for setup, usage, and testing |
| `Dockerfile` | Docker image blueprint | Defines how to build the application container |
| `docker-compose.yml` | Container orchestration | Configures port mapping, volumes, and environment |
| `.github/workflows/ci.yml` | CI/CD Pipeline | GitHub Actions workflow for automated testing and validation |
| `app.py` | Flask application | Entry point for the API server |
| `config.py` | Configuration settings | Database URI, JWT secrets, token expiration |
| `models.py` | Database models | User, Event, RSVP SQLAlchemy classes |
| `openapi.yaml` | API specification | OpenAPI 3.0 spec for Swagger UI |
| `requirements.txt` | Python dependencies | All pip packages needed to run |

### File Responsibilities

| File | Purpose | Key Components |
|------|---------|-----------------|
| `app.py` | Application factory | `create_app()`, blueprint registration, JWT init |
| `config.py` | Settings & secrets | `SECRET_KEY`, `JWT_SECRET_KEY`, database URI, token expiration |
| `models.py` | Database models | `User`, `Event`, `RSVP` classes with relationships |
| `routes/auth.py` | Authentication | `/register` (POST), `/login` (POST) |
| `routes/events.py` | Event CRUD | `/events` (GET, POST), `/events/{id}` (GET) |
| `routes/rsvps.py` | RSVP system | `/rsvps/event/{id}` (POST, GET) with access control |
| `tests/conftest.py` | Test fixtures | `base_url`, `unique_user_credentials`, `authenticated_headers` |
| `tests/test_models.py` | Unit tests | 5 database model tests (password, serialization, counting) |
| `tests/test_api.py` | Integration tests | 12 HTTP endpoint tests (happy paths + error cases) |
| `.github/workflows/ci.yml` | CI/CD automation | Build image, run tests, health checks, cleanup

### Docker Files Explanation

#### Dockerfile

The `Dockerfile` at the root directory contains:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["python", "app.py"]
```

**Configuration Details:**
- **Base Image**: `python:3.11-slim` - Lightweight Python 3.11 runtime for optimal performance
- **Working Directory**: `/app` - All application code copied here
- **Dependency Installation**: Installs all packages from `requirements.txt` in one layer
- **Port Exposure**: `4000` - Matches Flask application port configuration
- **Startup Command**: `python app.py` - Runs Flask development server

**Environment Variables (set in docker-compose.yml):**
- `FLASK_APP=app.py` - Points Flask to the application entry point
- `FLASK_RUN_HOST=0.0.0.0` - Binds Flask to all network interfaces (required for container communication)
- `FLASK_RUN_PORT=4000` - Sets Flask to listen on port 4000

#### docker-compose.yml

The `docker-compose.yml` at the root directory contains:
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "4000:4000"
    environment:
      - FLASK_APP=app.py
      - FLASK_RUN_PORT=4000
    volumes:
      - .:/app
    command: python app.py
```

**Purpose**: Orchestrates the Docker container with:
- Automatic image building from Dockerfile
- Port mapping (container 4000 → local 4000)
- Environment variables for Flask configuration
- Volume mounting for live code reloading during development
- Container startup command

---

### Directory Structure Details

#### `.github/` Directory - CI/CD Workflows

```
.github/
└── workflows/
    └── ci.yml
```

| File | Purpose |
|------|---------|
| `ci.yml` | GitHub Actions CI pipeline - Triggers on push/PR to main, builds Docker image, runs all 17 tests, cleans up container |

---

#### `instance/` Directory - Application Data

```
instance/
└── events.db
```

| File | Purpose |
|------|---------|
| `events.db` | SQLite database file (auto-created by Flask-SQLAlchemy on first run) - Contains user, event, rsvp tables |

---

#### `routes/` Directory - API Endpoints

```
routes/
├── __init__.py
├── auth.py
├── events.py
└── rsvps.py
```

| File | Purpose |
|------|---------|
| `__init__.py` | Package initializer (empty file marking this directory as a Python package) |
| `auth.py` | Authentication blueprint - POST /api/auth/register (user creation), POST /api/auth/login (JWT generation) |
| `events.py` | Event management blueprint - GET /api/events (list), POST /api/events (create), GET /api/events/{id} (get single) |
| `rsvps.py` | RSVP system blueprint - POST /api/rsvps/event/{id} (RSVP), GET /api/rsvps/event/{id} (view RSVPs with stats) |

---

#### `tests/` Directory - Test Suite

```
tests/
├── __init__.py
├── conftest.py
├── test_models.py
└── test_api.py
```

| File | Purpose |
|------|---------|
| `__init__.py` | Package initializer (empty file marking this directory as a Python package) |
| `conftest.py` | Pytest configuration and shared fixtures (base_url, unique_user_credentials, authenticated_headers) |
| `test_models.py` | Unit tests (5 tests) - Tests User, Event, RSVP model serialization and password hashing |
| `test_api.py` | Integration tests (12 tests) - Tests all API endpoints with running Flask server on localhost:4000 |

---

## 🐳 Docker Setup & Usage Guide

### 1. Local Setup and Build

Use these commands to build your image and start the container locally using Docker Compose.

**⚠️ Important Architecture Note:**
If you're developing on a **Mac system**, the `docker-compose.yml` includes `platform: linux/amd64` to ensure compatibility with Render hosting. This forces Docker to build for the Linux AMD64 architecture even on Mac, preventing deployment failures.

**Build and Start:**
```bash
docker compose up -d --build
```

**Check Status:**
```bash
docker ps
```

**Access API:**
Open `http://localhost:4000/events` in your browser.

---

### 2. Pushing to Docker Hub

To share your image, you must tag it and push it to your repository.

**Login:**
```bash
docker login
```

**Tag Version:**
```bash
docker tag abhisakh/events-api:latest abhisakh/events-api:v1.0
```

**Push Image:**
```bash
docker push abhisakh/events-api:v1.0
```

---

### 3. Pulling and Running from Registry

If you are on a new machine, you can pull the image directly without the source code.

**Pull Image:**
```bash
docker pull abhisakh/events-api:latest
```

**Run Container:**
```bash
docker run -d -p 4000:4000 --name events-container abhisakh/events-api:latest
```

---

### 4. Testing the Docker Container

Once the container is running, verify the setup with these tests.

**Health Check:**
```bash
curl http://localhost:4000/api/health
```

**Run Integration Tests:**
```bash
pytest -v
```
*(Ensure the container is "Up" first)*

**View Internal Logs:**
```bash
docker logs -f events-container
```

---

### 5. Management Tips

**Stop Project:**
```bash
docker compose stop
```

**Full Cleanup:**
```bash
docker compose down
```

**Inspect Files:**
Use the Files tab in Docker Desktop to see the `/app` directory.

---

## 🐳 Docker Configuration

### Dockerfile

The `Dockerfile` is the blueprint for your application environment. It ensures that every instance of the app runs with the exact same dependencies and settings.

**Key Features:**
- **Base Image**: Uses `python:3.9-slim` to provide a lightweight and efficient runtime
- **Automation**: Handles the installation of all libraries from `requirements.txt` automatically
- **Portability**: Packages the source code so it can run on any system with Docker installed

**Typical Dockerfile Structure:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["python", "app.py"]
```

---

### docker-compose.yml

This file acts as the control panel for your container. It defines how the image interacts with your computer's hardware and network.

**Key Features:**
- **One-Command Setup**: Allows you to build and start the entire project using `docker compose up -d`
- **Port Mapping**: Bridges the container to your local machine (e.g., `4000:4000`) so the API is accessible at `localhost`
- **Environment Control**: Sets critical Flask variables like `FLASK_APP` and `FLASK_RUN_PORT` dynamically
- **Platform Specification**: Ensures compatibility across different architectures (Intel/AMD vs Mac)

**docker-compose.yml Structure:**
```yaml
version: '3.8'

services:
  api:
    platform: linux/amd64
    build: .
    image: abhisakh/events-api
    container_name: events-container
    ports:
      - "4000:4000"
    environment:
      - FLASK_APP=app.py
      - FLASK_RUN_HOST=0.0.0.0
      - FLASK_RUN_PORT=4000
```

**Critical Configuration Details:**

| Configuration | Value | Purpose |
|---------------|-------|---------|
| `platform` | `linux/amd64` | Forces build/run on Linux AMD64 architecture (required for Render compatibility) |
| `build` | `.` | Builds image from Dockerfile in current directory |
| `image` | `abhisakh/events-api` | Names the image for Docker Hub push |
| `container_name` | `events-container` | Sets container name for easy reference |
| `ports` | `4000:4000` | Maps container port 4000 to local port 4000 |
| `FLASK_RUN_HOST` | `0.0.0.0` | Binds Flask to all network interfaces (required for container networking) |
| `FLASK_RUN_PORT` | `4000` | Sets Flask internal port to 4000 |

**Platform Architecture Explanation:**

The `platform: linux/amd64` line is **CRITICAL** for cross-platform compatibility:

- **Mac Systems** use `linux/arm64` architecture (Apple Silicon) or `darwin/amd64` (Intel Mac)
- **Render Hosting** only supports `linux/amd64` (standard Linux server architecture)
- **GitHub Actions CI** runs on `linux/amd64` by default

**Without this specification:**
- ❌ Mac users build images in `linux/arm64`
- ❌ Images won't run on Render (architecture mismatch)
- ❌ Deployment fails: `Error: exec format error`

**With this specification:**
- ✅ All developers build `linux/amd64` images regardless of their OS
- ✅ Images work seamlessly on Render
- ✅ CI/CD pipeline compatible
- ✅ Production deployments succeed

---

## 🏗️ Docker Architecture Compatibility

### The Platform Specification Problem

When developing on different operating systems, Docker can build images for different CPU architectures:

| OS | Default Architecture | Docker Build Output |
|----|----------------------|----------------------|
| **Mac (Apple Silicon)** | `linux/arm64` | ARM64 Linux image |
| **Mac (Intel)** | `linux/amd64` | AMD64 Linux image |
| **Linux (Intel/AMD)** | `linux/amd64` | AMD64 Linux image |
| **Windows** | `linux/amd64` | AMD64 Linux image |

### Why This Matters for Render

Render hosting infrastructure uses **Linux servers with AMD64 architecture** exclusively.

**Scenario Without `platform: linux/amd64`:**
```
Mac Developer builds image
    ↓
Docker creates linux/arm64 image (Apple Silicon default)
    ↓
Image pushed to Docker Hub as abhisakh/events-api:latest
    ↓
Render pulls image
    ↓
❌ FATAL ERROR: exec format error
   (Render expects linux/amd64, got linux/arm64)
```

**Scenario With `platform: linux/amd64`:**
```
Mac Developer builds image
    ↓
Docker Buildx emulates linux/amd64
    ↓
Image created in correct architecture
    ↓
Image pushed to Docker Hub as abhisakh/events-api:latest
    ↓
Render pulls image
    ↓
✅ SUCCESS: Image runs perfectly
```

### How to Verify Architecture

**Check your image architecture:**
```bash
docker image inspect abhisakh/events-api | grep -i architecture
```

**Expected output:**
```json
"Architecture": "amd64"
```

### Common Architecture Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `exec format error` on Render | Wrong architecture (arm64 instead of amd64) | Add `platform: linux/amd64` to docker-compose.yml |
| Image builds slowly on Mac | Emulation overhead | Expected behavior - Buildx emulates architecture |
| Different sizes for same image | Different architectures have different sizes | Verify with `docker image inspect` |
| Can't run on Linux after building on Mac | Architecture mismatch | Rebuild with `platform: linux/amd64` specified |

---

### Local Development

To build and run the project locally for the first time:

```bash
docker compose up -d --build
```

**Access the API:**
- Browser: `http://localhost:4000/events`
- Health Check: `http://localhost:4000/api/health`

**Run Tests:**
```bash
# Ensure the container is active, then run
pytest -v
```

---

### Deployment & Distribution

To share your image with others via Docker Hub:

1. **Login to Docker Hub:**
   ```bash
   docker login
   ```

2. **Tag Your Image:**
   ```bash
   docker tag abhisakh/events-api:latest abhisakh/events-api:v1.0
   ```

3. **Push to Registry:**
   ```bash
   docker push abhisakh/events-api:v1.0
   ```

---

### Running from the Cloud

To run the project on a new machine without the source code:

```bash
# Pull the image from Docker Hub
docker pull abhisakh/events-api:latest

# Run the container
docker run -d -p 4000:4000 --name events-container abhisakh/events-api:latest
```

**Verify It's Running:**
```bash
curl http://localhost:4000/api/health
```

---

### 🛠 Troubleshooting & Management

| Task | Command |
|------|---------|
| Stop the App | `docker compose stop` |
| Remove Container | `docker compose down` |
| View Logs | `docker compose logs -f` |
| Inspect Files | Use Files tab in Docker Desktop |
| Rebuild Image | `docker compose up -d --build` |
| Full Reset | `docker compose down -v` (removes volumes) |

**View Container Status:**
```bash
docker ps
```

**Check Container Details:**
```bash
docker inspect events-container
```

---

## ⚙️ CI/CD Pipeline - GitHub Actions Workflow (Version 5)

### Overview

The **GitHub Actions CI/CD pipeline** (`ci.yml`) automates the complete software delivery process:
- **CI Job**: Builds, tests, and validates your application locally
- **CD Job**: Publishes to Docker Hub and deploys to Render production

**Workflow Name**: "From Dev to Prod 5 – Deploying the Events API"

**Workflow File Location**: `.github/workflows/ci.yml`

**Trigger Events**:
- ✅ Push to `main` branch
- ✅ Pull requests targeting `main` branch

---

### Complete Pipeline Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                   GitHub Actions CI/CD Pipeline (v5)                         │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  🔄 TRIGGER: Push to main OR Pull Request                                   │
│           │                                                                  │
│           ▼                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    📋 CI JOB: TEST (Always Runs)                    │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                     │   │
│  │  1️⃣  Checkout Code                                                 │   │
│  │  2️⃣  Set up Docker Buildx                                          │   │
│  │  3️⃣  Build Docker Image (linux/amd64 + caching)                    │   │
│  │  4️⃣  Run Containerized API (localhost:4000)                        │   │
│  │  5️⃣  Health Check (curl /api/health)                               │   │
│  │  6️⃣  Install Python 3.9 dependencies                               │   │
│  │  7️⃣  Run pytest -v (17 tests)                                      │   │
│  │  8️⃣  Cleanup container                                             │   │
│  │                                                                     │   │
│  │  ✅ Result: PASS → Proceed to CD                                    │   │
│  │  ❌ Result: FAIL → STOP (No deployment)                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│           │                                                                  │
│           ▼ (Only if CI passes)                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │            🚀 CD JOB: DEPLOY (Conditional on CI Success)            │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │  Environment: production                                            │   │
│  │  Requires: test job success                                         │   │
│  │                                                                     │   │
│  │  1️⃣  Checkout Code                                                 │   │
│  │  2️⃣  Login to Docker Hub                                           │   │
│  │  3️⃣  Set up Docker Buildx                                          │   │
│  │  4️⃣  Build & Push Production Image (3 tags):                       │   │
│  │      └─► latest (for current version)                              │   │
│  │      └─► {SHA} (exact commit hash)                                 │   │
│  │      └─► {BRANCH} (branch name)                                    │   │
│  │  5️⃣  Trigger Render Webhook                                        │   │
│  │  6️⃣  Wait 60s for Render rollout                                   │   │
│  │  7️⃣  Live Smoke Test (/api/health on Render)                       │   │
│  │                                                                     │   │
│  │  ✅ Result: All tests pass → Production live!                       │   │
│  │  ❌ Result: Any test fails → Rollback (Render still has old image) │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│           │                                                                  │
│           ▼                                                                  │
│  🎉 APPLICATION LIVE ON RENDER                                              │
│     https://events-api-latest-rsgk.onrender.com                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### CI Job: Build, Test, and Clean

**Purpose**: Validates code quality and functionality before deployment

**Key Features**:

#### 1️⃣ Checkout Code
```yaml
- name: Checkout Code
  uses: actions/checkout@v4
```
- Clones repository into CI environment
- Makes all code available for building and testing

#### 2️⃣ Set up Docker Buildx
```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3
```
- Enables advanced Docker building features
- Supports multi-platform builds and caching

#### 3️⃣ Build Docker Image
```yaml
- name: Build Docker Image
  uses: docker/build-push-action@v5
  with:
    context: .
    file: ./Dockerfile
    load: true
    platforms: linux/amd64
    tags: abhisakh/events-api:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

**Significance of Each Parameter**:

| Parameter | Value | Why It Matters |
|-----------|-------|----------------|
| `platforms: linux/amd64` | ✨ **NEW** Explicitly specified | Ensures compatibility with Render (no arm64 issues) |
| `load: true` | Load into Docker daemon | Makes image available for local testing in CI |
| `cache-from: type=gha` | GitHub Actions cache | Reuses previous build layers (60-80% faster) |
| `cache-to: type=gha,mode=max` | Full cache storage | Stores all layers for maximum reuse |

#### 4️⃣ Run Containerized API
```yaml
- name: Run Containerized API
  run: |
    docker run -d \
      -p 4000:4000 \
      --name events-container \
      abhisakh/events-api:latest
```
- Starts the built image as a running container
- Maps port 4000 for HTTP requests
- Names container for cleanup reference

#### 5️⃣ Health Check
```yaml
- name: Wait for API and Check Health
  run: |
    echo "Waiting for API to start..."
    sleep 3
    curl --fail --verbose http://localhost:4000/api/health
```
- Waits 3 seconds for Flask initialization
- Makes HTTP request to health endpoint
- Fails pipeline if health check fails (--fail flag)

#### 6️⃣ Setup Python & Dependencies
```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.9'
    cache: 'pip'

- name: Install Dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```
- Python 3.9 (matches project requirements)
- `cache: 'pip'` saves dependencies for faster runs
- Installs pytest and all test requirements

#### 7️⃣ Run Test Suite
```yaml
- name: Run Test Suite
  run: |
    pytest -v
```
- Executes all 17 tests (5 unit + 12 integration)
- `-v` flag provides verbose output
- Tests run against localhost:4000 (from conftest.py)

#### 8️⃣ Cleanup Container
```yaml
- name: Clean up Container
  if: always()
  runs: |
    if [ "$(docker ps -aq -f name=events-container)" ]; then
      docker stop events-container
      docker rm events-container
    else
      echo "No container found to clean up."
    fi
```
- `if: always()` - Runs even if tests fail
- Stops and removes container completely
- Frees up resources for next run
- Prevents port conflicts

---

### CD Job: Publish, Deploy, and Smoke Test

**Purpose**: Releases validated code to production on Render

**Key Features**:

#### Job Configuration
```yaml
deploy:
  name: Publish, Deploy, and Smoke Test
  needs: test
  runs-on: ubuntu-latest
  environment: production
```

**Significance**:

| Configuration | Significance |
|---------------|-------------|
| `needs: test` | ✨ **CRITICAL** Only runs if CI job succeeds - prevents bad code from reaching production |
| `environment: production` | ✨ **NEW** Marks as production environment, enforces GitHub protection rules |
| `runs-on: ubuntu-latest` | Same runner as CI job, consistent environment |

#### 1️⃣ Checkout Code
```yaml
- name: Checkout Code
  uses: actions/checkout@v4
```
- Gets fresh code for building production image

#### 2️⃣ Docker Hub Login
```yaml
- name: Log in to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_HUB_USERNAME }}
    password: ${{ secrets.DOCKER_HUB_TOKEN }}
```

**Significance**:
- Authenticates with Docker Hub using GitHub Secrets
- Must use correct secret names (no underscores)
- Enables push to private/public repositories

#### 3️⃣ Set up Docker Buildx
```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3
```
- Same as CI, enables advanced features for CD build

#### 4️⃣ Build and Push Production Image
```yaml
- name: Build and Push Production Image
  uses: docker/build-push-action@v5
  with:
    context: .
    file: ./Dockerfile
    push: true
    platforms: linux/amd64
    tags: |
      abhisakh/events-api:latest
      abhisakh/events-api:${{ github.sha }}
      abhisakh/events-api:${{ github.ref_name }}
```

**Significance - Three Tag Strategy** ✨ **NEW**:

| Tag | Value Example | Purpose |
|-----|--------------|---------|
| `latest` | `abhisakh/events-api:latest` | Always points to current production version |
| `${{ github.sha }}` | `abhisakh/events-api:a1b2c3d4...` | Exact commit hash - perfect for rollback |
| `${{ github.ref_name }}` | `abhisakh/events-api:main` | Branch name - identifies which branch deployed |

**Why Multiple Tags Matter**:
- **`latest`** - Render always pulls this tag
- **`SHA`** - If production breaks, can rollback to previous commit
- **`branch`** - Track which branch is in production

#### 5️⃣ Trigger Render Deployment
```yaml
- name: Trigger Render Deployment
  run: |
    echo "Triggering deployment via Render Webhook..."
    curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK }}"
```

**Significance**:
- HTTP POST to Render webhook URL
- Signals Render to pull latest image from Docker Hub
- Automatic deployment without manual intervention

#### 6️⃣ Wait for Render Rollout
```yaml
- name: Wait for Render Rollout
  run: |
    echo "Waiting 60 seconds for Render to deploy the new image..."
    sleep 60
```

**Significance** ✨ **NEW**:
- Waits 60 seconds for Render to:
  - Pull image from Docker Hub
  - Start new container
  - Replace old container
  - Reach stable state
- Prevents premature smoke test on old version

#### 7️⃣ Automated Smoke Test Against Live Render
```yaml
- name: Automated Smoke Test Against Live Render API
  run: |
    echo "Running smoke test against live production deployment..."
    curl --fail --verbose "${{ secrets.RENDER_BASE_URL }}/api/health"
```

**Significance** ✨ **NEW**:
- Makes HTTP request to **live production URL**
- Verifies production deployment succeeded
- If fails, alerts team to deployment issue
- Tests actual user-facing endpoint

---

### Workflow Execution Timeline

```
Total Time: ~5-8 minutes

0:00 → 0:30   Checkout, Docker Buildx setup, Build image      (~30s)
0:30 → 1:00   Run container, health check, Python setup       (~30s)
1:00 → 2:00   Install dependencies, Run 17 tests              (~60s)
2:00 → 2:30   Cleanup container                               (~30s)

           ↓ (CI passes - CD starts)

2:30 → 3:00   Checkout, Docker Hub login, Buildx setup        (~30s)
3:00 → 4:00   Build & Push image with 3 tags                  (~60s)
4:00 → 4:30   Trigger Render webhook                          (~30s)
4:30 → 5:30   Wait for Render rollout                         (~60s)
5:30 → 5:45   Smoke test against live production              (~15s)

5:45          🎉 Deployment complete! App live on Render
```

---

### Critical Improvements in Version 5

| Feature | Version 4 | Version 5 | Impact |
|---------|-----------|-----------|--------|
| Architecture | Not specified | `platforms: linux/amd64` | ✨ Fixes Render compatibility |
| Job separation | Single job | Two jobs (test + deploy) | ✨ Prevents bad code from reaching prod |
| Environment | Not marked | `environment: production` | ✨ Enforces GitHub protection rules |
| Image tags | `latest` only | 3 tags (latest, SHA, branch) | ✨ Enables rollback capability |
| Render wait | Immediate | 60 second wait | ✨ Ensures deployment completes |
| Live smoke test | Not in CD | Against Render URL | ✨ Verifies production is up |
| Python version | 3.11 | 3.9 | Adjusted for compatibility |

---

### Failure Scenarios and Recovery

**Scenario 1: CI Tests Fail**
```
Push to main
  ↓
CI job runs and fails (pytest fails)
  ↓
❌ CD job NEVER runs (needs: test)
  ↓
Production remains unchanged
  ↓
Developer fixes issue and pushes again
```

**Scenario 2: CI Passes, CD Fails at Live Smoke Test**
```
Push to main
  ↓
CI job passes all tests
  ↓
CD job builds and pushes image
  ↓
Render receives webhook and deploys
  ↓
❌ Live smoke test fails (e.g., database connection issue)
  ↓
GitHub Actions marks deployment as failed
  ↓
⚠️ Render is still running new image (but broken)
  ↓
Developer must manually rollback to previous image tag or restart old container
```

**Scenario 3: Complete Success**
```
Push to main
  ↓
✅ CI all tests pass
  ↓
✅ CD builds image with 3 tags
  ↓
✅ Image pushed to Docker Hub
  ↓
✅ Render webhook triggered
  ↓
✅ Wait 60 seconds for rollout
  ↓
✅ Live smoke test passes
  ↓
🎉 Production live and verified!
```

---

### Secrets Required for CI/CD

See [GitHub Actions Secrets Configuration](#-github-actions-secrets-configuration) section for complete details.

Required secrets:
- `DOCKER_HUB_USERNAME` - Docker Hub account username
- `DOCKER_HUB_TOKEN` - Docker Hub Personal Access Token
- `RENDER_DEPLOY_HOOK` - Render webhook URL
- `RENDER_BASE_URL` - Production URL for smoke testing

---

---

### Pipeline Stages Explained

#### **Stage 1: Checkout Code**

```yaml
- name: Checkout Code
  uses: actions/checkout@v4
```

**Purpose**: Clone the repository code into the CI runner environment

**What Happens**:
- GitHub fetches the latest code from the branch
- All files are available for building and testing
- Code is ready for Docker image build

---

#### **Stage 2: Docker Build & Setup**

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build Docker Image
  uses: docker/build-push-action@v5
  with:
    context: .
    file: ./Dockerfile
    load: true
    tags: events-api:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

**Purpose**: Build the Docker image with intelligent caching

**What Happens**:
- ✅ Sets up Docker Buildx (advanced build capabilities)
- ✅ Reads `Dockerfile` from root directory
- ✅ Builds image with tag `events-api:latest`
- ✅ **Cache optimization**: Uses GitHub Actions cache (`gha`) for faster builds
- ✅ `load: true` loads image into local Docker daemon for testing

**Why Cache Matters**:
- Subsequent builds are 60-80% faster
- Avoids re-downloading dependencies
- Layers are cached (base image, pip installs, etc.)

---

#### **Stage 3: Run Containerized API**

```yaml
- name: Run Containerized API
  run: |
    docker run -d \
      -p 4000:4000 \
      --name events-container \
      events-api:latest

- name: Wait for API and Check Health
  run: |
    echo "Waiting for API to start..."
    sleep 3
    curl --fail --verbose http://localhost:4000/api/health
```

**Purpose**: Start the API container and verify it's healthy

**What Happens**:
- ✅ Runs container in detached mode (`-d`)
- ✅ Maps port 4000 (container) → 4000 (CI environment)
- ✅ Names container `events-container` for easy reference
- ✅ Waits 3 seconds for Flask to initialize
- ✅ Makes HTTP request to `/api/health` endpoint
- ✅ Fails pipeline if health check returns non-200 status

**Health Check Response**:
```json
{
    "status": "healthy"
}
```

---

#### **Stage 4: Install Dependencies & Run Tests**

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.9'
    cache: 'pip'

- name: Install Dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt

- name: Run Test Suite
  run: |
    pytest -v
```

**Purpose**: Run the complete test suite against the running container

**What Happens**:
- ✅ Installs Python 3.9 (matches project requirements)
- ✅ Caches pip packages for faster runs
- ✅ Installs all dependencies from `requirements.txt`
- ✅ Runs pytest with verbose output (`-v`)
- ✅ Executes all 17 tests:
  - 5 unit tests (test_models.py)
  - 12 integration tests (test_api.py)

**Test Configuration**:
- Tests connect to running container on `http://localhost:4000`
- Base URL from `conftest.py`: `BASE_URL = "http://localhost:4000"`
- Fixtures auto-setup users and JWT tokens

**Test Results**:
```
test_health_endpoint_returns_healthy PASSED
test_register_user_creates_new_user PASSED
test_login_returns_jwt_token PASSED
test_create_public_event_requires_auth_and_succeeds_with_token PASSED
test_rsvp_to_public_event_succeeds_without_auth PASSED
test_get_all_events_returns_list PASSED
test_duplicate_username_registration_returns_400 PASSED
test_create_event_without_auth_returns_401 PASSED
test_rsvp_to_non_public_event_without_auth_returns_error PASSED
test_get_invalid_event_id_returns_404 PASSED
test_create_event_with_missing_required_fields_returns_400 PASSED
test_rsvp_to_non_existent_event_returns_404 PASSED
test_user_password_hashing_behaves_correctly PASSED
test_user_to_dict_conversion PASSED
test_event_to_dict_empty_rsvps PASSED
test_event_to_dict_with_mocked_rsvps_calculates_counts PASSED
test_rsvp_to_dict_conversion PASSED

======================== 17 passed in 4.23s ========================
```

---

#### **Stage 5: Cleanup**

```yaml
- name: Clean up Container
  if: always()
  runs: |
    if [ "$(docker ps -aq -f name=events-container)" ]; then
      echo "Stopping and removing container..."
      docker stop events-container
      docker rm events-container
    else
      echo "No container found to clean up."
    fi
```

**Purpose**: Remove container after tests complete (even if tests fail)

**What Happens**:
- ✅ Runs regardless of previous step success/failure (`if: always()`)
- ✅ Checks if `events-container` exists
- ✅ Stops the running container
- ✅ Removes the container completely
- ✅ Frees up resources on CI runner

**Why This Matters**:
- Prevents container accumulation
- Ensures clean environment for next run
- Avoids port conflicts (4000 still available)

---

### GitHub Actions Workflow Details

#### File: `.github/workflows/ci.yml`

**Workflow Name**: "From Dev to Prod 4 – CI with GitHub Actions"

**Runs On**: `ubuntu-latest` (latest Ubuntu runner)

**Jobs**:
- Single job: `test` (Build, Test, and Clean)

**Trigger Conditions**:
```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

Runs when:
- ✅ Code pushed to `main` branch
- ✅ Pull request created targeting `main`
- ✅ Pull request updated with new commits

---

### Pipeline Execution Timeline

```
┌────────────────────────────────────────────────────────────────────┐
│                    Typical Pipeline Run                            │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│ Checkout Code                    ████                  ~2s        │
│ Set up Docker Buildx             ███                   ~1s        │
│ Build Docker Image               ██████████████        ~15s       │
│ Run Containerized API            ████                  ~2s        │
│ Wait & Health Check              ███                   ~3s        │
│ Set up Python                    ██████                ~6s        │
│ Install Dependencies             █████████             ~10s       │
│ Run Test Suite                   ██████████████████    ~20s       │
│ Clean up Container               ██                    ~1s        │
│                                                                    │
│                    Total: ~60 seconds                              │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

### Monitoring Pipeline Runs

#### View Pipeline Status on GitHub

1. **Go to Repository** → `Actions` tab
2. **Select Workflow**: "From Dev to Prod 4 – CI with GitHub Actions"
3. **View Recent Runs**: Shows status (✅ Passed / ❌ Failed)
4. **Click Run**: See detailed logs for each stage

#### Pipeline Status Badge

Add to your README:
```markdown
[![CI Pipeline](https://github.com/YOUR_USERNAME/evently-api/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/evently-api/actions)
```

---

### CI Pipeline Best Practices

| Best Practice | Implementation |
|---------------|-----------------|
| **Cache Dependencies** | `cache: 'pip'` in setup-python |
| **Docker Layer Caching** | `cache-from: type=gha, cache-to: type=gha,mode=max` |
| **Health Checks** | `curl http://localhost:4000/api/health` |
| **Always Cleanup** | `if: always()` ensures cleanup even on failure |
| **Fail Fast** | `--fail` flag on curl makes pipeline fail on health check failure |
| **Verbose Output** | `pytest -v` shows each test result |
| **Version Pinning** | Actions use pinned versions (`@v4`, `@v5`) |

---

### Troubleshooting CI Failures

| Error | Cause | Solution |
|-------|-------|----------|
| `Connection refused on localhost:4000` | API didn't start | Check Docker logs: `docker logs events-container` |
| `pytest: command not found` | Requirements not installed | Verify `requirements.txt` includes pytest |
| `Port 4000 already in use` | Previous container not cleaned | Manually run `docker stop events-container && docker rm events-container` |
| `curl: (28) operation timeout` | API startup too slow | Increase sleep time from 3 to 5 seconds |
| `Cache miss on Docker layers` | First build or cache cleared | Second run will be faster with caching |

---

### Continuous Deployment (CD) Job

**Purpose**: Automates the release and live deployment to production on Render.

**Steps Performed:**
1. **Docker Hub Authentication** - Logs in with `secrets.DOCKERHUB_USERNAME` and `secrets.DOCKERHUB_TOKEN`
2. **Build Production Image** - Builds Docker image from production Dockerfile
3. **Tag Image** - Tags with multiple versions:
   - `latest` - Latest stable release
   - Commit SHA - Exact git commit reference
   - Branch name - Development/main branch reference
4. **Push to Docker Hub** - Pushes all tagged images to `abhisakh/events-api` repository
5. **Trigger Render Deployment** - Calls `RENDER_DEPLOY_HOOK` webhook to signal Render
6. **Smoke Test** - Runs final verification: `curl --fail --verbose "${{ secrets.RENDER_BASE_URL }}/api/health"`

**Critical Fixes Applied:**
- ✅ Corrected secret names: `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` (no underscores)
- ✅ Created matching credentials in GitHub Repository Secrets
- ✅ Fixed `Error: Username and password required` failure
- ✅ Configured Render webhook integration

---

## 🔐 GitHub Actions Secrets Configuration

All sensitive credentials are stored securely in GitHub Repository Secrets. Navigate to:
**Settings > Secrets and variables > Actions > Repository secrets**

### Required Secrets

| Secret Name | Value | Purpose | How to Retrieve |
|-------------|-------|---------|-----------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username (abhisakh) | Docker Hub authentication | Docker Hub account profile page |
| `DOCKERHUB_TOKEN` | Personal Access Token (PAT) | CLI authentication (instead of password) | Docker Hub Account Settings > Security > New Access Token |
| `RENDER_DEPLOY_HOOK` | Unique webhook URL from Render | Triggers deployment when image is pushed | Render Dashboard > Web Service > Settings > Deploy Hook |
| `RENDER_BASE_URL` | Production URL (https://events-api-latest-rsgk.onrender.com) | Final smoke test endpoint | Render Dashboard service page |

### How to Create Docker Hub PAT (Personal Access Token)

1. Go to Docker Hub > Account Settings > Security
2. Click "New Access Token"
3. Give it a name: `github-actions`
4. Grant read/write permissions
5. Copy token and add to GitHub Secrets as `DOCKERHUB_TOKEN`

### How to Get Render Deploy Hook

1. Go to Render Dashboard > Web Service (`events-api-latest-rsgk`)
2. Navigate to Settings > Deploy Hook
3. Copy the webhook URL
4. Add to GitHub Secrets as `RENDER_DEPLOY_HOOK`

---

## 🚀 Render Deployment Platform – Significance & Usage

### What is Render?

**Render** is a cloud hosting platform that:
- ✅ Automatically deploys Docker containers from Docker Hub
- ✅ Manages networking, SSL/HTTPS, and domain routing
- ✅ Scales horizontally with increased traffic
- ✅ Provides automatic backups and monitoring
- ✅ Integrates seamlessly with GitHub webhooks
- ✅ Offers free tier for educational/testing projects

### Why Render for This Project?

| Aspect | Significance |
|--------|-------------|
| **Docker-Native** | Pulls images from Docker Hub, no code repository needed |
| **Zero-Configuration** | Automatic SSL, networking, and environment setup |
| **Webhook Integration** | Deploys automatically when new image is pushed |
| **Scalability** | Easy to upgrade from free tier to paid plans |
| **Monitoring** | Real-time logs and health monitoring |
| **linux/amd64** | Natively supports this architecture (no Mac compatibility issues) |

### Render vs Traditional Hosting

| Feature | Traditional Server | Heroku | AWS | Render |
|---------|-------------------|--------|-----|--------|
| **Deploy Docker** | Manual/Complex | Limited | Complex setup | ✅ Native |
| **GitHub Webhooks** | Manual setup | ✅ Easy | ✅ But complex | ✅ Easy |
| **SSL Certificates** | Manual renewal | ✅ Auto | ✅ But complex | ✅ Auto |
| **Scaling** | Manual provisioning | Easy | Complex | ✅ Easy |
| **Cost** | Varies | $5+/month | $0-1000+/month | Free tier + Pay-as-you-go |
| **Learning Curve** | Steep | Medium | Very steep | ✅ Low |

---

## 🚀 Render Deployment Details

Your application is hosted on Render with automatic deployment via GitHub Actions webhook.

### Service Configuration

| Detail | Value | Significance |
|--------|-------|-------------|
| **Service Name** | `events-api-latest-rsgk` | Unique identifier in Render dashboard |
| **Service Type** | Web Service | Runs containerized application |
| **Internal Port** | `4000` | Container listens on port 4000 |
| **Exposed Port** | `443` (HTTPS) / `80` (HTTP) | Public-facing ports |
| **Production URL** | `https://events-api-latest-rsgk.onrender.com` | Live application endpoint |
| **Docker Image** | `abhisakh/events-api:latest` | Pulled from Docker Hub |
| **Deployment Trigger** | GitHub Actions webhook | Automatic on image push |
| **Health Check Path** | `/api/health` | Render monitors this endpoint |
| **Health Check Interval** | Every 30 seconds | Automatic monitoring |

### Health Check Endpoint

Render continuously monitors your application health by calling:

**Local Development**: `http://localhost:4000/api/health`

**Production (Live)**: `https://events-api-latest-rsgk.onrender.com/api/health`

**Expected Response** (200 OK):
```json
{
    "status": "healthy"
}
```

**What Render Does**:
- ✅ Checks health every 30 seconds
- ✅ If healthy (200) → Application is live
- ✅ If unhealthy (5xx) → Marks service as failing
- ✅ If no response → Service offline, may trigger restart

### Automatic Deployment Flow

```
┌──────────────────────────────────────────────────────────────────────┐
│                    RENDER DEPLOYMENT FLOW                            │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  1️⃣  Developer pushes code to main branch                           │
│      └─► GitHub receives push event                                 │
│                                                                      │
│  2️⃣  GitHub Actions CI pipeline runs                                │
│      └─► Runs 17 tests in Docker container                          │
│      └─► If any test fails → STOP (no deployment)                   │
│                                                                      │
│  3️⃣  CI passes → CD job starts                                      │
│      └─► Builds Docker image with 3 tags                            │
│      └─► Pushes to Docker Hub (abhisakh/events-api)                 │
│                                                                      │
│  4️⃣  GitHub Actions triggers Render webhook                         │
│      └─► Sends POST to RENDER_DEPLOY_HOOK URL                       │
│      └─► Payload: {deploy_hook_id, ref, sha}                        │
│                                                                      │
│  5️⃣  Render receives webhook signal                                 │
│      └─► Verifies webhook signature                                 │
│      └─► Starts new deployment                                      │
│                                                                      │
│  6️⃣  Render pulls image from Docker Hub                             │
│      └─► Pulls: abhisakh/events-api:latest                          │
│      └─► Verifies image integrity                                   │
│                                                                      │
│  7️⃣  Render starts new container                                    │
│      └─► Allocates resources (CPU, RAM)                             │
│      └─► Maps port 4000 → 443 (HTTPS)                               │
│      └─► Sets environment variables                                 │
│                                                                      │
│  8️⃣  Health check phase                                             │
│      └─► Waits for application startup                              │
│      └─► Calls /api/health every 5 seconds                          │
│      └─► Waits for 200 OK response                                  │
│                                                                      │
│  9️⃣  Old container cleanup                                          │
│      └─► Gracefully shuts down old container                        │
│      └─► Traffic automatically routed to new container              │
│                                                                      │
│  🔟 GitHub Actions smoke test                                       │
│      └─► Calls https://events-api-latest-rsgk.onrender.com/api/health
│      └─► If healthy → Deployment success! ✅                        │
│      └─► If unhealthy → Marks as failed ❌                          │
│                                                                      │
│  ✅ APPLICATION LIVE ON RENDER                                      │
│     https://events-api-latest-rsgk.onrender.com                     │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

### Render Usage Guide

#### 1️⃣ Accessing Your Service

**Dashboard**: https://dashboard.render.com
- View service status
- Check recent deployments
- Monitor logs in real-time
- Adjust environment variables

**Live Application**: https://events-api-latest-rsgk.onrender.com
- Test endpoints directly
- Run API calls
- Check health: https://events-api-latest-rsgk.onrender.com/api/health

#### 2️⃣ Viewing Deployment Logs

**In Render Dashboard**:
1. Go to Service → "events-api-latest-rsgk"
2. Click "Logs" tab
3. See real-time output from:
   - Container startup
   - Flask initialization
   - Requests and responses
   - Errors (if any)

**What to Look For**:
```
✅ "Running on http://0.0.0.0:4000"    → Application started
✅ "GET /api/health"                   → Health check passed
❌ "ERROR" or exceptions                → Investigation needed
❌ "Address already in use"             → Port conflict
```

#### 3️⃣ Checking Service Status

**Healthy Status** (🟢 Green):
```
- Recent deployments successful
- Health check passes
- No error logs
- Application responding
```

**Unhealthy Status** (🔴 Red):
```
- Deployment failed
- Health check timing out
- Application crashes
- Port unavailable
```

#### 4️⃣ Manual Deployment (If Needed)

If you need to redeploy without pushing code:

**Option 1: Redeploy Last Build**
1. Go to Render Dashboard → Service
2. Click "Manual Deploy" → "Deploy latest"
3. Render pulls last image from Docker Hub

**Option 2: Force New Build**
1. Push a dummy commit: `git commit --allow-empty -m "Trigger redeploy"`
2. Push to main: `git push origin main`
3. GitHub Actions automatically rebuilds and redeploys

**Option 3: Update Image Tag**
1. Edit CD job to push new tag
2. Update Render to pull from new tag
3. Manual redeploy from dashboard

#### 5️⃣ Environment Variables

To set environment variables in Render:

1. Go to Service → "events-api-latest-rsgk"
2. Click "Environment" tab
3. Add variables:
   ```
   FLASK_APP=app.py
   FLASK_RUN_HOST=0.0.0.0
   FLASK_RUN_PORT=4000
   ```
4. Click "Save" → Automatic redeploy

#### 6️⃣ Rollback to Previous Version

If current deployment has issues:

**Using Docker Tags**:
1. Note the SHA tag of last good deployment (from logs)
2. Update Render to pull from `abhisakh/events-api:{OLD_SHA}`
3. Manual Deploy from dashboard
4. Old version live immediately

**Using Branch Tags**:
1. Update to `abhisakh/events-api:main`
2. Manual Deploy from dashboard

#### 7️⃣ Monitoring & Alerts

**Built-in Monitoring**:
- Real-time logs
- Deployment history
- Health check status
- Resource usage (CPU, RAM)

**Set Up Alerts** (Premium):
1. Service Settings → Notifications
2. Email alerts on deployment failure
3. Slack integration available

---

### Common Render Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **Container won't start** | Port already in use / Memory limit | Check logs, increase resources |
| **Health check failing** | App crashes on startup | View logs, check environment vars |
| **Webhook not triggering** | Wrong webhook URL / expired token | Regenerate deploy hook in Render |
| **Image not found error** | Docker Hub image deleted | Push new image and redeploy |
| **Slow deployment** | Large image size / network latency | Expected, wait 2-3 minutes |
| **SSL certificate error** | DNS not configured | Render auto-generates, wait 24h |
| **503 Service Unavailable** | Container restarting | Check logs for crash reasons |

---

## 🌐 Webhook & Environment Details

### Render Deployment Webhook

**Source**: Generated in Render Service Settings

**How It Works:**
1. GitHub Actions successfully pushes image to Docker Hub
2. Workflow triggers POST request to `RENDER_DEPLOY_HOOK`
3. Render receives webhook signal
4. Render pulls fresh image tag from Docker Hub repository
5. New container deployed to production on port 4000
6. Application automatically available at `https://events-api-latest-rsgk.onrender.com`

### Port Configuration

- **Container Internal Port**: `4000`
- **Environment Variable**: `FLASK_RUN_PORT=4000`
- **Render Exposed Port**: `4000`
- **Public URL**: Maps to port `443` (HTTPS) / `80` (HTTP)

### OpenAPI Specification

The `openapi.yaml` file documents all API endpoints:
- **Server URL (Local)**: `http://localhost:4000`
- **Server URL (Production)**: `https://events-api-latest-rsgk.onrender.com`
- **Base Path**: `/api`
- **Health Check Path**: `/api/health` (Used in deployment verification)

### Environment Variables in Production

These are automatically set by Render:
- `FLASK_APP=app.py`
- `FLASK_RUN_HOST=0.0.0.0` (Required for container networking)
- `FLASK_RUN_PORT=4000`
- `FLASK_ENV=production` (Can be set in Render service settings)

---

## 📋 Deployment Checklist

Before your first production deployment, verify:

- ✅ Dockerfile uses `python:3.11-slim`
- ✅ Port `4000` is exposed in Dockerfile
- ✅ Environment variables set in docker-compose.yml
- ✅ All 4 GitHub Actions Secrets configured
- ✅ `RENDER_DEPLOY_HOOK` tested and working
- ✅ Docker Hub repository is public or accessible
- ✅ CI/CD workflow passes all tests
- ✅ Production URL reachable and health check returns 200

---

## 🚀 Getting Started

### Installation

```bash
git clone <repository-url>
cd evently-api

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Run Server

```bash
python app.py
# Server at http://localhost:4000
```

### Run Tests

```bash
# Terminal 1: python app.py (keep running)
# Terminal 2:
pytest -v
```

---

## 📦 conftest.py - Test Configuration & Fixtures

**Purpose**: Centralizes pytest configuration, shared fixtures, and utilities used across all test modules.

### Configuration Constants

```python
BASE_URL = "http://localhost:4000"
```

- Defines the API server endpoint for all integration tests
- Centralized configuration - easy to update if port changes
- Used by all HTTP request operations

---

### Fixture 1: `base_url` (Session Scope)

**Signature**: `@pytest.fixture(scope="session")`

**Purpose**: Provides the base URL for the running API server.

**Returns**: `"http://localhost:4000"`

**Scope**: Session-level (created once per test session)

**Usage Example**:
```python
def test_health_endpoint(base_url):
    response = requests.get(f"{base_url}/api/health")
```

**Why Session Scope?**:
- URL doesn't change during test execution
- Improves performance by creating once
- Shared across all tests

---

### Fixture 2: `unique_user_credentials` (Function Scope)

**Signature**: `@pytest.fixture`

**Purpose**: Generates guaranteed unique username credentials using millisecond-precision timestamps.

**Returns**:
```python
{
    "username": "user_1737283920123",
    "password": "SecurePassword123"
}
```

**Implementation**:
```python
timestamp = int(time.time() * 1000)  # Milliseconds since epoch
return {
    "username": f"user_{timestamp}",
    "password": "SecurePassword123"
}
```

**Key Features**:
- ✅ Timestamp in **milliseconds** ensures uniqueness
- ✅ Function-scoped: New credentials for each test
- ✅ Prevents database conflicts from duplicate usernames
- ✅ Allows tests to run repeatedly without cleanup

**Why Milliseconds?**:
- Multiple tests can run in the same second
- Millisecond precision prevents collisions
- Example: `user_1737283920123` vs `user_1737283920456`

**Usage Example**:
```python
def test_register_user(base_url, unique_user_credentials):
    response = requests.post(
        f"{base_url}/api/auth/register",
        json=unique_user_credentials
    )
    # username is unique every time this test runs
```

---

### Fixture 3: `authenticated_headers` (Function Scope)

**Signature**: `@pytest.fixture`

**Purpose**: Automatically registers a user, logs them in, and returns authorization headers containing a valid JWT token.

**Dependencies**:
- `base_url` fixture
- `unique_user_credentials` fixture

**Returns**:
```python
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Implementation Flow**:
```python
def authenticated_headers(base_url, unique_user_credentials):
    # Step 1: Register a new user
    requests.post(
        f"{base_url}/api/auth/register",
        json=unique_user_credentials
    )

    # Step 2: Login with registered credentials
    login_response = requests.post(
        f"{base_url}/api/auth/login",
        json=unique_user_credentials
    )

    # Step 3: Extract JWT token
    token = login_response.json().get("access_token")

    # Step 4: Return formatted authorization header
    return {"Authorization": f"Bearer {token}"}
```

**Why This Fixture Is Powerful**:
- ✅ Eliminates boilerplate: Tests don't repeat registration/login
- ✅ Automatic setup: Fresh authenticated user for each test
- ✅ Clean syntax: Tests simply request `authenticated_headers`
- ✅ Realistic: Mimics actual user authentication flow

**Usage Example**:
```python
def test_create_event(base_url, authenticated_headers):
    # Headers already contain valid JWT token
    response = requests.post(
        f"{base_url}/api/events",
        json={"title": "My Event", "date": "2026-06-01"},
        headers=authenticated_headers  # Authentication handled!
    )
```

**Token Format**:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.payload.signature
```
- Prefix: `"Bearer "` (note the space)
- Token: JWT with header, payload, and signature
- Valid until expiration (1 hour, configurable in config.py)

**JWT Claims**:
```python
{
    "sub": user_id,          # Subject (user ID as string)
    "iat": issued_timestamp, # Issued at time
    "exp": expiration_time,  # Expiration time (1 hour later)
    "is_admin": True/False   # Admin flag from user record
}
```

---

---

## 📦 File 2: `test_models.py` - Unit Tests (5 Tests)

**Philosophy**: Pure unit tests validating database model logic in complete isolation. Execute entirely in Python memory with **no database persistence, no HTTP requests, no external dependencies**.

---

### ✅ Test 1: `test_user_password_hashing_behaves_correctly`

**Function Name**: `test_user_password_hashing_behaves_correctly()`

**Category**: User Model - Security

**Purpose**: Verifies that password hashing and verification mechanism works correctly using werkzeug security.

**What It Tests**:
- ✅ `set_password()` method hashes plaintext passwords
- ✅ Passwords are **never stored in plaintext**
- ✅ `check_password()` correctly verifies valid passwords
- ✅ `check_password()` correctly rejects invalid passwords

**Test Implementation**:
```python
def test_user_password_hashing_behaves_correctly():
    # Create User instance in memory
    user = User()
    user.username = "test_user"
    user.set_password("SecureSecretPass123!")

    # Raw password text is never exposed explicitly
    assert user.password_hash != "SecureSecretPass123!"

    assert user.check_password("SecureSecretPass123!") is True

    # Assert wrong password verification correctly fails
    assert user.check_password("WrongPassword123") is False
```

**Security Mechanisms**:
- Uses werkzeug's `generate_password_hash()` and `check_password_hash()`
- One-way cryptographic hashing (cannot reverse)
- Automatic salting prevents rainbow table attacks
- Each hash is unique even for identical passwords

**Assertions Breakdown**:

| Assertion | What It Validates | Why It Matters |
|-----------|-------------------|----------------|
| `password_hash != plaintext` | Hash is created, not plaintext stored | Prevents credential exposure |
| `check_password(correct) == True` | Valid credentials are accepted | Users can log in |
| `check_password(wrong) == False` | Invalid credentials are rejected | Prevents unauthorized access |

**Why This Test Matters**:
- Password security is foundational to authentication
- Prevents database compromise from exposing passwords
- Validates the security layer works before deployment

---

### ✅ Test 2: `test_user_to_dict_conversion`

**Function Name**: `test_user_to_dict_conversion()`

**Category**: User Model - Serialization

**Purpose**: Validates dictionary output matching the expected layout framework structure.

**What It Tests**:
- ✅ `to_dict()` method returns all required fields
- ✅ Timestamps are ISO 8601 formatted strings
- ✅ No sensitive data (password_hash) in output
- ✅ Boolean and integer types preserved

**Test Implementation**:
```python
def test_user_to_dict_conversion():
    """Unit Test: Validates dictionary output matching the expected layout framework structure."""
    fixed_time = datetime(2026, 5, 18, 12, 0, 0)

    user = User(
        id=42,
        username="admin_guy",
        is_admin=True,
        created_at=fixed_time
    )

    user_dict = user.to_dict()

    assert user_dict["id"] == 42
    assert user_dict["username"] == "admin_guy"
    assert user_dict["is_admin"] is True
    assert user_dict["created_at"] == "2026-05-18T12:00:00"
```

**Expected Dictionary Output**:
```python
{
    "id": 42,
    "username": "admin_guy",
    "is_admin": True,
    "created_at": "2026-05-18T12:00:00"
}
```

**Field Specifications**:

| Field | Type | Format | Notes |
|-------|------|--------|-------|
| `id` | int | Integer | Primary key |
| `username` | str | String | Unique identifier |
| `is_admin` | bool | Boolean | Role flag |
| `created_at` | str | ISO 8601 | "YYYY-MM-DDTHH:MM:SS" |

**What's Excluded** (Security):
- ❌ `password_hash` - Never exposed in API responses
- ❌ Internal database fields

**Why This Test Matters**:
- API responses must return consistent, well-formatted data
- Prevents accidental exposure of sensitive fields
- Ensures frontend clients receive expected data structure
- Validates datetime serialization works correctly

---

### ✅ Test 3: `test_event_to_dict_empty_rsvps`

**Function Name**: `test_event_to_dict_empty_rsvps()`

**Category**: Event Model - Serialization (Empty State)

**Purpose**: Validates event dictionary exports correctly when there are zero attendees.

**What It Tests**:
- ✅ `to_dict()` handles zero RSVPs gracefully
- ✅ Returns empty list for `attendees` (not null)
- ✅ `rsvp_count` correctly calculates as 0
- ✅ All event metadata fields included

**Test Implementation**:
```python
def test_event_to_dict_empty_rsvps():
    """Unit Test: Validates event dictionary exports correctly when there are zero attendees."""
    fixed_time = datetime(2026, 6, 1, 15, 30, 0)

    event = Event(
        id=101,
        title= "Tech Conference",
        description="A great developer meetup",
        date=fixed_time,
        location="Room A",
        capacity=100,
        is_public=True,
        requires_admin=False,
        created_by=42,
        created_at=fixed_time,
        rsvps=[] # Explicitly pass empty list to mock relationship
    )

    event_dict = event.to_dict()

    assert event_dict["id"] == 101
    assert event_dict["title"] == "Tech Conference"
    assert event_dict["rsvp_count"] == 0
    assert event_dict["attendees"] == []
```

**Expected Dictionary Output**:
```python
{
    "id": 101,
    "title": "Tech Conference",
    "description": "A great developer meetup",
    "date": "2026-06-01T15:30:00",
    "location": "Room A",
    "capacity": 100,
    "is_public": True,
    "requires_admin": False,
    "created_by": 42,
    "created_at": "2026-06-01T15:30:00",
    "rsvp_count": 0,
    "attendees": []
}
```

**Key Validations**:

| Field | Expected Value | Why It Matters |
|-------|---------------|----------------|
| `rsvp_count` | `0` | Count of RSVPs (total) |
| `attendees` | `[]` | Empty list, not null | Prevents frontend errors |

**Edge Case Handling**:
- Empty list `[]` vs `null` - JavaScript/JSON safety
- Zero count clearly indicates no RSVPs
- Consistent structure regardless of data presence

**Why This Test Matters**:
- Most common initial state for new events
- Prevents null pointer exceptions in frontend
- Validates boundary condition handling
- Ensures API doesn't break on empty relationships

---

### ✅ Test 4: `test_event_to_dict_with_mocked_rsvps_calculates_counts`

**Function Name**: `test_event_to_dict_with_mocked_rsvps_calculates_counts()`

**Category**: Event Model - Serialization (With Data)

**Purpose**: Validates tracking calculations for event RSVPs without interacting with DB engines.

**What It Tests**:
- ✅ `to_dict()` correctly processes RSVP relationships
- ✅ `rsvp_count` counts **all** RSVPs (total count)
- ✅ `attendees` list only includes `attending=True` user IDs
- ✅ Declined RSVPs excluded from attendees list

**Test Implementation**:
```python
def test_event_to_dict_with_mocked_rsvps_calculates_counts():
    """Unit Test: Validates tracking calculations for event RSVPs without interacting with DB engines."""
    fixed_time = datetime(2026, 6, 1, 15, 30, 0)

    # simulate relationship tables
    rsvp1 = RSVP(user_id=11, attending=True)
    rsvp2 = RSVP(user_id=12, attending=False) # Not attending, shouldn't show in user list
    rsvp3 = RSVP(user_id=13, attending=True)

    event = Event(
        id=202,
        title="Exclusive Workshop",
        date=fixed_time,
        rsvps=[rsvp1, rsvp2, rsvp3]
    )

    event_dict = event.to_dict()

    # Total linked records counted
    assert event_dict["rsvp_count"] == 3

    # Only active, attending user IDs filtered out into final listing array
    assert event_dict["attendees"] == [11, 13]
```

**Business Logic Validation**:

```python
# Total RSVP Count (all responses)
rsvp_count = len(event.rsvps)  # 3 (includes True and False)

# Attendees List (only attending=True)
attendees = [rsvp.user_id for rsvp in event.rsvps if rsvp.attending]
# Result: [11, 13]
```

**RSVP Filtering Logic**:

| User ID | Attending Status | Included in `rsvp_count`? | Included in `attendees`? |
|---------|-----------------|--------------------------|-------------------------|
| 11 | `True` | ✅ Yes | ✅ Yes |
| 12 | `False` | ✅ Yes | ❌ No |
| 13 | `True` | ✅ Yes | ✅ Yes |

**Expected Output**:
```python
{
    "id": 202,
    "title": "Exclusive Workshop",
    "date": "2026-06-01T15:30:00",
    "rsvp_count": 3,         # Total responses
    "attendees": [11, 13]    # Only user IDs with attending=True
}
```

**Why This Test Matters**:
- Accurate attendance counting is critical for capacity management
- Prevents overbooking events
- Tests core business logic for event management
- Validates filtering of declined RSVPs
- Ensures attendee list accuracy for event organizers

---

### ✅ Test 5: `test_rsvp_to_dict_conversion`

**Function Name**: `test_rsvp_to_dict_conversion()`

**Category**: RSVP Model - Serialization

**Purpose**: Validates RSVP properties populate dictionary mapping arrays cleanly.

**What It Tests**:
- ✅ `to_dict()` returns all required RSVP fields
- ✅ Foreign keys (user_id, event_id) preserved
- ✅ Boolean `attending` status correctly included
- ✅ Timestamps properly formatted

**Test Implementation**:
```python
def test_rsvp_to_dict_conversion():
    """Unit Test: Validates RSVP properties populate dictionary mapping arrays cleanly."""
    fixed_time = datetime(2026, 5, 18, 16, 0, 0)

    rsvp = RSVP(
        id=7,
        event_id=101,
        user_id=11,
        attending=True,
        created_at=fixed_time
    )

    rsvp_dict = rsvp.to_dict()

    assert rsvp_dict["id"] == 7
    assert rsvp_dict["event_id"] == 101
    assert rsvp_dict["user_id"] == 11
    assert rsvp_dict["attending"] is True
    assert rsvp_dict["created_at"] == "2026-05-18T16:00:00"
```

**Expected Dictionary Output**:
```python
{
    "id": 7,
    "event_id": 101,
    "user_id": 11,
    "attending": True,
    "created_at": "2026-05-18T16:00:00"
}
```

**Field Specifications**:

| Field | Type | Purpose | Notes |
|-------|------|---------|-------|
| `id` | int | Primary key | Auto-generated |
| `event_id` | int | Foreign key | Links to Event |
| `user_id` | int | Foreign key | Links to User |
| `attending` | bool | Status flag | True = attending, False = declined |
| `created_at` | str | Timestamp | ISO 8601 format |

**Relational Integrity**:
- `event_id` → References `Event.id`
- `user_id` → References `User.id`
- Links users to events with attendance status

**Why This Test Matters**:
- RSVPs are the bridge between users and events
- Validates relational data is preserved
- Ensures API responses have consistent RSVP structure
- Critical for displaying attendee lists

---

## 📦 File 3: `test_api.py` - Integration Tests (8 Tests)

**Philosophy**: End-to-end integration tests that validate complete HTTP request/response cycles. Send real HTTP requests to a **running Flask server** on `http://localhost:4000`.

**Prerequisites**:
- ⚠️ **CRITICAL**: Flask server MUST be running on `localhost:4000`
- Tests will fail if server is not accessible

---

## 🟢 Happy Path Tests (6 Tests)

### ✅ Test 6: `test_health_endpoint_returns_healthy`

**Function Name**: `test_health_endpoint_returns_healthy(base_url)`

**Category**: Integration - Health Check

**Purpose**: Check server running health status.

**What It Tests**:
- ✅ Server is running and accessible
- ✅ Health endpoint responds with 200 status
- ✅ Response contains "healthy" indicator

**HTTP Request**:
```http
GET http://localhost:4000/api/health
```

**Test Implementation**:
```python
def test_health_endpoint_returns_healthy(base_url):
    """Happy Path 1: Check server running health status."""
    response = requests.get(f"{base_url}/api/health")
    assert response.status_code == 200
    assert "healthy" in response.text.lower() or response.json().get("status") == "healthy"
```

**Expected Response** (200 OK):
```json
{
    "status": "healthy"
}
```

**Assertions**:
- ✅ Status code = `200`
- ✅ Response contains "healthy" (case-insensitive) OR
- ✅ Response JSON has `status: "healthy"`

**Why This Test Matters**:
- First test to run - validates server is running
- Confirms basic HTTP infrastructure works
- Used for monitoring and health checks

**Common Failures**:
- ❌ `ConnectionError` - Server not running
- ❌ Wrong port - Server on 5000 instead of 4000

---

### ✅ Test 7: `test_register_user_creates_new_user`

**Function Name**: `test_register_user_creates_new_user(base_url, unique_user_credentials)`

**Category**: Integration - Authentication

**Purpose**: Register a user with a unique timestamped name.

**What It Tests**:
- ✅ User registration succeeds
- ✅ Returns 201 Created status
- ✅ User object included in response
- ✅ Username matches request payload

**Fixtures Used**:
- `base_url` - API endpoint
- `unique_user_credentials` - Generated username with timestamp

**HTTP Request**:
```http
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920123",
    "password": "SecurePassword123"
}
```

**Test Implementation**:
```python
def test_register_user_creates_new_user(base_url, unique_user_credentials):
    """Happy Path 2: Register a user with a unique timestamped name."""
    response = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert response.status_code == 201
    assert response.json()["user"]["username"] == unique_user_credentials["username"]
```

**Expected Response** (201 Created):
```json
{
    "message": "User created successfully",
    "user": {
        "id": 1,
        "username": "user_1737283920123",
        "is_admin": false,
        "created_at": "2026-05-19T10:30:00"
    }
}
```

**Assertions**:
- ✅ Status code = `201 Created`
- ✅ Response contains `user` object
- ✅ Username matches the request payload

**Validation Points**:
- User successfully created in database
- Username uniqueness enforced (tested separately)
- Password hashed before storage (unit test validates)
- Response excludes password_hash

**Why This Test Matters**:
- Registration is user entry point
- Validates database write operations
- Tests first step of authentication flow

---

### ✅ Test 8: `test_login_returns_jwt_token`

**Function Name**: `test_login_returns_jwt_token(base_url, unique_user_credentials)`

**Category**: Integration - Authentication

**Purpose**: Log in with known user and retrieve a JWT.

**What It Tests**:
- ✅ Login endpoint works with valid credentials
- ✅ Returns 200 OK status
- ✅ Response contains JWT access_token
- ✅ User object returned with token

**Fixtures Used**:
- `base_url` - API endpoint
- `unique_user_credentials` - Fresh user credentials

**Test Flow**:
1. Register a new user (setup)
2. Login with registered credentials
3. Validate JWT token received

**HTTP Requests**:
```http
# Step 1: Register
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920456",
    "password": "SecurePassword123"
}

# Step 2: Login
POST http://localhost:4000/api/auth/login
Content-Type: application/json

{
    "username": "user_1737283920456",
    "password": "SecurePassword123"
}
```

**Test Implementation**:
```python
def test_login_returns_jwt_token(base_url, unique_user_credentials):
    """Happy Path 3: Log in with known user and retrieve a JWT."""
    # Register the user first
    requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)

    # Attempt login
    response = requests.post(f"{base_url}/api/auth/login", json=unique_user_credentials)
    assert response.status_code == 200
    assert "access_token" in response.json()
```

**Expected Response** (200 OK):
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzI4MzkyMCwianRpIjoiYWJjMTIzIiwibmJmIjoxNzM3MjgzOTIwLCJzdWIiOjEsInR5cGUiOiJhY2Nlc3MifQ.signature",
    "user": {
        "id": 1,
        "username": "user_1737283920456",
        "is_admin": false
    }
}
```

**JWT Token Structure**:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImlhdCI6MTczNzI4MzkyMH0.signature
```
- Part 1: Header (algorithm, token type)
- Part 2: Payload (user ID, issued at, expiration)
- Part 3: Signature (cryptographic verification)

**Assertions**:
- ✅ Status code = `200 OK`
- ✅ Response contains `access_token` field
- ✅ Token is a non-empty string

**Why This Test Matters**:
- JWT tokens enable stateless authentication
- Tests second step of authentication flow
- Validates token generation works correctly

---

### ✅ Test 9: `test_create_public_event_requires_auth_and_succeeds_with_token`

**Function Name**: `test_create_public_event_requires_auth_and_succeeds_with_token(base_url, authenticated_headers)`

**Category**: Integration - Event Management

**Purpose**: Call POST /events with a valid JWT payload.

**What It Tests**:
- ✅ Event creation with JWT authentication works
- ✅ Returns 201 Created status
- ✅ Event data correctly persisted
- ✅ All event fields in response

**Fixtures Used**:
- `base_url` - API endpoint
- `authenticated_headers` - JWT token headers (auto-setup)

**HTTP Request**:
```http
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Public Networking Event",
    "date": "2026-06-01",
    "is_public": true
}
```

**Test Implementation**:
```python
def test_create_public_event_requires_auth_and_succeeds_with_token(base_url, authenticated_headers):
    """Happy Path 4: Call POST /events with a valid JWT payload."""
    event_payload = {
        "title": "Public Networking Event",
        "date": "2026-06-01",
        "is_public": True
    }
    response = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    assert response.status_code == 201
    assert response.json().get("title") == "Public Networking Event"
```

**Expected Response** (201 Created):
```json
{
    "id": 1,
    "title": "Public Networking Event",
    "date": "2026-06-01T00:00:00",
    "is_public": true,
    "requires_admin": false,
    "capacity": null,
    "location": null,
    "description": null,
    "rsvps": [],
    "rsvp_count": 0,
    "attendees": [],
    "created_at": "2026-05-19T10:30:00"
}
```

**Assertions**:
- ✅ Status code = `201 Created`
- ✅ Response title matches request payload

**Authentication Validation**:
- Requires valid JWT token in Authorization header
- Token automatically provided by `authenticated_headers` fixture
- User must be authenticated to create events

**Why This Test Matters**:
- Event creation is core platform feature
- Validates JWT authentication for protected endpoints
- Ensures only authenticated users can create events

---

### ✅ Test 10: `test_rsvp_to_public_event_succeeds_without_auth`

**Function Name**: `test_rsvp_to_public_event_succeeds_without_auth(base_url, authenticated_headers)`

**Category**: Integration - RSVP System

**Purpose**: Create a public event first, then RSVP without any auth token.

**What It Tests**:
- ✅ Public events allow unauthenticated RSVPs
- ✅ Returns 200/201 status
- ✅ RSVP created with correct event_id
- ✅ No authentication required for public events

**Fixtures Used**:
- `base_url` - API endpoint
- `authenticated_headers` - Used only for event creation

**Test Flow**:
1. Create a public event (with auth)
2. RSVP to event (without auth)
3. Validate RSVP succeeds

**HTTP Requests**:
```http
# Step 1: Create Public Event (authenticated)
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Open House",
    "date": "2026-07-01",
    "is_public": true
}

# Step 2: RSVP (NO authentication header)
POST http://localhost:4000/api/rsvps/event/1
Content-Type: application/json

{}
```

**Test Implementation**:
```python
def test_rsvp_to_public_event_succeeds_without_auth(base_url, authenticated_headers):
    """Happy Path 5: Create a public event first, then RSVP without any auth token."""
    # Create the public event with credentials
    event_payload = {"title": "Open House", "date": "2026-07-01", "is_public": True}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")

    # RSVP without using authenticated headers
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    assert rsvp_res.status_code in [200, 201]
    assert rsvp_res.json().get("event_id") == event_id
```

**Expected Response** (200 OK or 201 Created):
```json
{
    "id": 1,
    "event_id": 1,
    "user_id": null,
    "attending": true,
    "created_at": "2026-05-19T10:30:00"
}
```

**Assertions**:
- ✅ Status code = `200` or `201`
- ✅ Response `event_id` matches created event

**Access Control Validation**:
- Public events (`is_public: true`) allow unauthenticated RSVPs
- No Authorization header required
- Anonymous users can RSVP

**Why This Test Matters**:
- Validates access control differentiates event types
- Ensures public events are truly accessible
- Tests unauthenticated API access paths

---

### ✅ Test 11: `test_get_all_events_returns_list`

**Function Name**: `test_get_all_events_returns_list(base_url)`

**Category**: Integration - Event Retrieval

**Purpose**: Verifies that fetching all events returns a 200 OK and a list layout.

**What It Tests**:
- ✅ GET /api/events returns 200 OK status
- ✅ Response is a list (array) type
- ✅ Empty list valid if no events exist

**HTTP Request**:
```http
GET http://localhost:4000/api/events
```

**Test Implementation**:
```python
def test_get_all_events_returns_list(base_url):
    """Happy Path: Verifies that fetching all events returns a 200 OK and a list layout."""
    response = requests.get(f"{base_url}/api/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

**Expected Response** (200 OK):
```json
[
    {
        "id": 1,
        "title": "Tech Conference",
        "date": "2026-06-01T15:30:00",
        "is_public": true,
        ...
    },
    {
        "id": 2,
        "title": "Workshop",
        "date": "2026-06-15T10:00:00",
        "is_public": false,
        ...
    }
]
```

**Assertions**:
- ✅ Status code = `200 OK`
- ✅ Response is a list (array) type
- ✅ Empty list `[]` is valid if no events exist

**Why This Test Matters**:
- Validates list endpoint structure
- Ensures proper JSON array response
- Tests read operations work correctly

---

## 🔴 Error Handling & Edge Case Tests (7 Tests)

### ✅ Test 12: `test_duplicate_username_registration_returns_400`

**Function Name**: `test_duplicate_username_registration_returns_400(base_url, unique_user_credentials)`

**Category**: Integration - Error Handling

**Purpose**: Registering duplicate username returns a bad request error.

**What It Tests**:
- ✅ First registration succeeds
- ✅ Duplicate username properly rejected
- ✅ Returns 400 Bad Request status
- ✅ Database constraint enforced

**Test Flow**:
1. Register user (succeeds)
2. Register same username again (fails)

**HTTP Requests**:
```http
# First Registration (succeeds)
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920789",
    "password": "SecurePassword123"
}

# Second Registration (fails)
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920789",
    "password": "SecurePassword123"
}
```

**Test Implementation**:
```python
def test_duplicate_username_registration_returns_400(base_url, unique_user_credentials):
    """Edge Case 1: Registering duplicate username returns a bad request error."""
    # First registration succeeds
    res1 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert res1.status_code == 201

    # Second registration with exact same username fails
    res2 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert res2.status_code == 400
```

**Expected Error Response** (400 Bad Request):
```json
{
    "error": "Username already exists",
    "message": "A user with this username is already registered"
}
```

**Assertions**:
- ✅ First registration: Status = `201 Created`
- ✅ Second registration: Status = `400 Bad Request`

**Why This Test Matters**:
- Validates username uniqueness constraint
- Tests error handling for constraint violations
- Prevents account conflicts

---

### ✅ Test 13: `test_create_event_without_auth_returns_401`

**Function Name**: `test_create_event_without_auth_returns_401(base_url)`

**Category**: Integration - Security

**Purpose**: Attempting to create an event with no token returns 401 Unauthorized.

**What It Tests**:
- ✅ Event creation requires authentication
- ✅ Missing token returns 401 Unauthorized status
- ✅ Event NOT created without auth

**HTTP Request**:
```http
POST http://localhost:4000/api/events
Content-Type: application/json
# NOTE: No Authorization header

{
    "title": "Secret Event",
    "date": "2026-08-01",
    "is_public": true
}
```

**Test Implementation**:
```python
def test_create_event_without_auth_returns_401(base_url):
    """Edge Case 2: Attempting to create an event with no token returns 401 Unauthorized."""
    event_payload = {"title": "Secret Event", "date": "2026-08-01", "is_public": True}
    response = requests.post(f"{base_url}/api/events", json=event_payload) # No headers sent
    assert response.status_code == 401
```

**Expected Error Response** (401 Unauthorized):
```json
{
    "msg": "Missing Authorization Header"
}
```

**Assertions**:
- ✅ Status code = `401 Unauthorized`
- ✅ Event NOT created

**Why This Test Matters**:
- Validates authentication is enforced
- Prevents unauthorized event creation
- Tests security boundary enforcement

---

### ✅ Test 14: `test_rsvp_to_non_public_event_without_auth_returns_error`

**Function Name**: `test_rsvp_to_non_public_event_without_auth_returns_error(base_url, authenticated_headers)`

**Category**: Integration - Access Control

**Purpose**: RSVPs to private events without a token are blocked.

**What It Tests**:
- ✅ Protected events require authentication
- ✅ Unauthenticated RSVP to private event rejected
- ✅ Returns 401/403/404 status
- ✅ RSVP NOT created

**Test Flow**:
1. Create private event (with auth)
2. RSVP to private event (without auth)
3. Validate rejection

**HTTP Requests**:
```http
# Step 1: Create Private Event
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Private Board Meeting",
    "date": "2026-09-01",
    "is_public": false
}

# Step 2: RSVP without auth (should fail)
POST http://localhost:4000/api/rsvps/event/1
Content-Type: application/json

{}
```

**Test Implementation**:
```python
def test_rsvp_to_non_public_event_without_auth_returns_error(base_url, authenticated_headers):
    """Edge Case 3: RSVPs to private events without a token are blocked."""
    # Create a private non-public event
    event_payload = {"title": "Private Board Meeting", "date": "2026-09-01", "is_public": False}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")

    # Attempt RSVP without authorization headers
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    assert rsvp_res.status_code in [401, 403, 404] # Depends on security setup
```

**Possible Error Responses**:
```json
// 401 Unauthorized
{
    "msg": "Missing Authorization Header"
}

// 403 Forbidden
{
    "error": "Access denied",
    "message": "This event requires authentication"
}

// 404 Not Found (if event hidden from unauthenticated users)
{
    "error": "Event not found"
}
```

**Assertions**:
- ✅ Status code = `401`, `403`, or `404`
- ✅ RSVP NOT created

**Access Control Matrix**:

| Event Type | `is_public` | RSVP Auth Required? |
|------------|-------------|---------------------|
| Public | `true` | No |
| Protected | `false` | Yes |

**Why This Test Matters**:
- Validates role-based access control
- Ensures private events remain private
- Tests multi-level authorization logic

---

### ✅ Test 15: `test_get_invalid_event_id_returns_404`

**Function Name**: `test_get_invalid_event_id_returns_404(base_url)`

**Category**: Integration - Error Handling

**Purpose**: Requesting an event ID that does not exist should yield a 404 Not Found.

**What It Tests**:
- ✅ Non-existent event returns 404 status
- ✅ Proper error handling for missing resources

**HTTP Request**:
```http
GET http://localhost:4000/api/events/999999
```

**Test Implementation**:
```python
def test_get_invalid_event_id_returns_404(base_url):
    """Edge Case: Requesting an event ID that does not exist should yield a 404 Not Found."""
    invalid_id = 999999
    response = requests.get(f"{base_url}/api/events/{invalid_id}")
    assert response.status_code == 404
```

**Expected Response** (404 Not Found):
```json
{
    "error": "Event not found"
}
```

**Assertions**:
- ✅ Status code = `404 Not Found`

**Why This Test Matters**:
- Validates proper HTTP status for missing resources
- Tests error handling for invalid IDs

---

### ✅ Test 16: `test_create_event_with_missing_required_fields_returns_400`

**Function Name**: `test_create_event_with_missing_required_fields_returns_400(base_url, authenticated_headers)`

**Category**: Integration - Input Validation

**Purpose**: Sending an event payload without a 'title' should trigger a 400 Bad Request.

**What It Tests**:
- ✅ Event creation requires all mandatory fields
- ✅ Missing title returns 400 status
- ✅ Input validation enforced
- ✅ Event NOT created with incomplete data

**HTTP Request**:
```http
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "date": "2026-12-01T12:00:00",
    "is_public": true
    // Missing "title" field
}
```

**Test Implementation**:
```python
def test_create_event_with_missing_required_fields_returns_400(base_url, authenticated_headers):
    """Edge Case: Sending an event payload without a 'title' should trigger a 400 Bad Request."""
    incomplete_payload = {
        "date": "2026-12-01T12:00:00",
        "is_public": True
    }
    response = requests.post(f"{base_url}/api/events", json=incomplete_payload, headers=authenticated_headers)
    assert response.status_code == 400
```

**Expected Response** (400 Bad Request):
```json
{
    "error": "Validation error",
    "message": "Missing required field: title"
}
```

**Assertions**:
- ✅ Status code = `400 Bad Request`
- ✅ Event NOT created

**Why This Test Matters**:
- Validates input validation works
- Ensures data integrity
- Tests required field enforcement

---

### ✅ Test 17: `test_rsvp_to_non_existent_event_returns_404`

**Function Name**: `test_rsvp_to_non_existent_event_returns_404(base_url, authenticated_headers)`

**Category**: Integration - Error Handling

**Purpose**: Attempting to RSVP to an event ID that does not exist should return a 404.

**What It Tests**:
- ✅ Non-existent event returns 404 status
- ✅ RSVP NOT created for invalid event
- ✅ Referential integrity enforced

**HTTP Request**:
```http
POST http://localhost:4000/api/rsvps/event/888888
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "attending": true
}
```

**Test Implementation**:
```python
def test_rsvp_to_non_existent_event_returns_404(base_url, authenticated_headers):
    """Edge Case: Attempting to RSVP to an event ID that does not exist should return a 404."""
    invalid_event_id = 888888
    response = requests.post(f"{base_url}/api/rsvps/event/{invalid_event_id}", json={"attending": True}, headers=authenticated_headers)
    assert response.status_code == 404
```

**Expected Response** (404 Not Found):
```json
{
    "error": "Event not found",
    "message": "Cannot RSVP to non-existent event"
}
```

**Assertions**:
- ✅ Status code = `404 Not Found`
- ✅ RSVP NOT created

**Why This Test Matters**:
- Validates referential integrity
- Tests error handling for invalid foreign keys

---

## 💾 Database Models

### Model 1: User

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    rsvps = db.relationship('RSVP', backref='user', lazy=True)
    events = db.relationship('Event', backref='creator', lazy=True)

    def set_password(password):
        # Hash plaintext password using werkzeug

    def check_password(password) -> bool:
        # Verify password against hash

    def to_dict() -> dict:
        # Returns: {id, username, is_admin, created_at}
        # Excludes: password_hash (security)
```

**Key Rules**:
- ✅ Username is unique
- ✅ First user becomes admin
- ✅ Password hashed before storage
- ✅ Password never exposed in responses

---

### Model 2: Event

```python
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    is_public = db.Column(db.Boolean, default=True, nullable=False)
    requires_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    rsvps = db.relationship('RSVP', backref='event', lazy=True, cascade='all, delete-orphan')

    def to_dict() -> dict:
        # Returns: {all fields above, rsvp_count, attendees}
        # rsvp_count = total RSVPs
        # attendees = user_ids where attending=True
```

**Access Control**:
| Type | `is_public` | `requires_admin` | RSVP Auth? |
|------|-------------|------------------|-----------|
| Public | True | False | No |
| Protected | False | False | Yes (any user) |
| Admin | False | True | Yes (admin only) |

---

### Model 3: RSVP

```python
class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    attending = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict() -> dict:
        # Returns: {id, event_id, user_id, attending, created_at}
```

**Key Points**:
- ✅ `user_id` can be None (anonymous RSVPs)
- ✅ `attending=True` means attending, `False` means declined
- ✅ One RSVP per user per event (POST updates existing)
- ✅ Capacity checks only count attending=True

---

## 🔌 API Reference

**Base URL**: `http://localhost:4000`

### Authentication

#### POST /api/auth/register
```json
{
    "username": "john_doe",
    "password": "SecurePassword123"
}
```
**Response** (201): `{message, user}`

#### POST /api/auth/login
```json
{
    "username": "john_doe",
    "password": "SecurePassword123"
}
```
**Response** (200): `{access_token, user}`

---

### Events

#### GET /api/events
**Response** (200): `[{event}, {event}, ...]`

#### POST /api/events (requires auth)
```json
{
    "title": "Python Meetup",
    "date": "2026-06-01",
    "description": "...",
    "location": "...",
    "capacity": 50,
    "is_public": true,
    "requires_admin": false
}
```
**Response** (201): `{event}`

#### GET /api/events/{event_id}
**Response** (200): `{event}` or (404): error

---

### RSVPs

#### POST /api/rsvps/event/{event_id}
```json
{
    "attending": true
}
```
**Response** (201/200): `{rsvp}`

#### GET /api/rsvps/event/{event_id}
**Response** (200): `{event, rsvps[], stats}`

---

## 🧪 Test Suite (13 Tests Total)

### conftest.py - Test Configuration & Fixtures

**Purpose**: Centralizes pytest configuration, shared fixtures, and utilities used across all test modules.

#### Configuration Constants

```python
BASE_URL = "http://localhost:4000"
```

- Defines the API server endpoint for all integration tests
- Centralized configuration - easy to update if port changes
- Used by all HTTP request operations

---

#### Fixture 1: `base_url` (Session Scope)

**Signature**: `@pytest.fixture(scope="session")`

**Purpose**: Provides the base URL for the running API server.

**Returns**: `"http://localhost:4000"`

**Scope**: Session-level (created once per test session)

**Usage Example**:
```python
def test_health_endpoint(base_url):
    response = requests.get(f"{base_url}/api/health")
```

**Why Session Scope?**:
- ✅ URL doesn't change during test execution
- ✅ Improves performance by creating once
- ✅ Shared across all tests

---

#### Fixture 2: `unique_user_credentials` (Function Scope)

**Signature**: `@pytest.fixture`

**Purpose**: Generates guaranteed unique username credentials using millisecond-precision timestamps.

**Returns**:
```python
{
    "username": "user_1737283920123",  # timestamp in milliseconds
    "password": "SecurePassword123"
}
```

**Implementation Details**:
```python
@pytest.fixture
def unique_user_credentials():
    timestamp = int(time.time() * 1000)  # Milliseconds since epoch
    return {
        "username": f"user_{timestamp}",
        "password": "SecurePassword123"
    }
```

**Key Features**:
- ✅ Timestamp in **milliseconds** ensures uniqueness
- ✅ Function-scoped: New credentials for each test
- ✅ Prevents database conflicts from duplicate usernames
- ✅ Allows tests to run repeatedly without cleanup

**Why Milliseconds?**:
- Multiple tests can run in the same second
- Millisecond precision prevents collisions
- Example: `user_1737283920123` vs `user_1737283920456`

**Usage Example**:
```python
def test_register_user(base_url, unique_user_credentials):
    response = requests.post(
        f"{base_url}/api/auth/register",
        json=unique_user_credentials
    )
    # username is unique every time this test runs
```

---

#### Fixture 3: `authenticated_headers` (Function Scope)

**Signature**: `@pytest.fixture`

**Purpose**: Automatically registers a user, logs them in, and returns authorization headers containing a valid JWT token.

**Dependencies**:
- `base_url` fixture
- `unique_user_credentials` fixture

**Returns**:
```python
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Implementation Flow**:
```python
@pytest.fixture
def authenticated_headers(base_url, unique_user_credentials):
    # Step 1: Register a new user
    requests.post(
        f"{base_url}/api/auth/register",
        json=unique_user_credentials
    )

    # Step 2: Login with registered credentials
    login_response = requests.post(
        f"{base_url}/api/auth/login",
        json=unique_user_credentials
    )

    # Step 3: Extract JWT token
    token = login_response.json().get("access_token")

    # Step 4: Return formatted authorization header
    return {"Authorization": f"Bearer {token}"}
```

**Why This Fixture Is Powerful**:
- ✅ Eliminates boilerplate: Tests don't repeat registration/login
- ✅ Automatic setup: Fresh authenticated user for each test
- ✅ Clean syntax: Tests simply request `authenticated_headers`
- ✅ Realistic: Mimics actual user authentication flow

**Usage Example**:
```python
def test_create_event(base_url, authenticated_headers):
    # Headers already contain valid JWT token
    response = requests.post(
        f"{base_url}/api/events",
        json={"title": "My Event", "date": "2026-06-01"},
        headers=authenticated_headers  # Authentication handled!
    )
```

**Token Format**:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzI4MzkyMCwianRpIjoiYWJjMTIzIiwibmJmIjoxNzM3MjgzOTIwLCJzdWIiOjEsInR5cGUiOiJhY2Nlc3MifQ.signature
```
- Prefix: `"Bearer "`
- Token: JWT with header, payload, and signature
- Valid until expiration (configurable in Flask app)

**Fixture Scope Explanation**:
- Function-scoped: Each test gets a fresh, unique authenticated user
- No test can interfere with another's authentication state
- Ensures test isolation and prevents cross-test contamination

---

### Test Execution Commands

```bash
# Run all tests
pytest -v

# Run specific test file
pytest tests/test_models.py -v

# Run specific test
pytest tests/test_api.py::test_register_user_creates_new_user -v

# Run tests matching pattern
pytest -k "rsvp" -v

# Run with coverage
pytest --cov=. --cov-report=html

# Run with detailed output
pytest -v -s

# Stop at first failure
pytest -x
```

---

### Unit Tests (test_models.py - 5 Tests)

| # | Test | Purpose |
|---|------|---------|
| 1 | `test_user_password_hashing_behaves_correctly` | Password hashing/verification works |
| 2 | `test_user_to_dict_conversion` | User serializes correctly to dict |
| 3 | `test_event_to_dict_empty_rsvps` | Event handles zero RSVPs |
| 4 | `test_event_to_dict_with_mocked_rsvps_calculates_counts` | RSVP counting and filtering works |
| 5 | `test_rsvp_to_dict_conversion` | RSVP serializes correctly to dict |

---

### Integration Tests (test_api.py - 8 Tests)

#### Happy Path (6 tests)

| # | Test | Validates |
|---|------|-----------|
| 6 | `test_health_endpoint_returns_healthy` | Server running, health check works |
| 7 | `test_register_user_creates_new_user` | User registration succeeds |
| 8 | `test_login_returns_jwt_token` | Login returns valid JWT |
| 9 | `test_create_public_event_requires_auth_and_succeeds_with_token` | Event creation with auth works |
| 10 | `test_rsvp_to_public_event_succeeds_without_auth` | Public event RSVP without auth works |
| 11 | `test_get_all_events_returns_list` | GET /api/events returns list |

#### Error Handling (7 tests)

| # | Test | Validates |
|---|------|-----------|
| 12 | `test_duplicate_username_registration_returns_400` | Duplicate username rejected |
| 13 | `test_create_event_without_auth_returns_401` | Event creation requires auth |
| 14 | `test_rsvp_to_non_public_event_without_auth_returns_error` | Protected event requires auth |
| 15 | `test_get_invalid_event_id_returns_404` | Non-existent event returns 404 |
| 16 | `test_create_event_with_missing_required_fields_returns_400` | Missing fields rejected |
| 17 | `test_rsvp_to_non_existent_event_returns_404` | RSVP to invalid event returns 404 |

---

## 🎓 Designing New Tests

### Template

```python
def test_[feature]_[condition]_[expected_outcome](fixtures):
    """Clear description."""

    # SETUP
    data = {...}

    # ACTION
    response = requests.post(f"{base_url}/api/endpoint", json=data, headers=headers)

    # ASSERTION
    assert response.status_code == expected_code
    assert response.json().get("field") == expected_value
```

### Example: Event Capacity

```python
def test_rsvp_respects_event_capacity(base_url, authenticated_headers):
    """Event capacity prevents overbooking."""

    # Create event with capacity=2
    event = {"title": "Small", "date": "2026-06-01", "capacity": 2, "is_public": True}
    event_res = requests.post(f"{base_url}/api/events", json=event, headers=authenticated_headers)
    event_id = event_res.json()["id"]

    # RSVP 1 and 2 (succeed)
    for i in range(2):
        rsvp = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
        assert rsvp.status_code in [200, 201]

    # RSVP 3 (fails)
    rsvp3 = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    assert rsvp3.status_code == 400
    assert "capacity" in rsvp3.json().get("error", "").lower()
```

### Example: Admin Access Control

```python
def test_admin_event_blocks_non_admin(base_url, authenticated_headers):
    """Only admins can RSVP to admin events."""

    # Create admin event
    event = {"title": "Admin", "date": "2026-06-01", "requires_admin": True, "is_public": False}
    event_res = requests.post(f"{base_url}/api/events", json=event, headers=authenticated_headers)
    event_id = event_res.json()["id"]

    # Create non-admin user
    non_admin = {"username": f"user_{int(time.time() * 1000) + 1}", "password": "SecurePassword123"}
    requests.post(f"{base_url}/api/auth/register", json=non_admin)
    login = requests.post(f"{base_url}/api/auth/login", json=non_admin)
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Non-admin RSVP fails
    rsvp = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={"attending": True}, headers=headers)
    assert rsvp.status_code == 403
    assert "admin" in rsvp.json().get("error", "").lower()
```

### Checklist

For each endpoint, test:
- [ ] Valid request succeeds
- [ ] Missing required fields returns 400
- [ ] Invalid data types returns 400
- [ ] Protected endpoints return 401 without auth
- [ ] Non-admin to admin endpoint returns 403
- [ ] Non-existent resources return 404
- [ ] Business logic enforced (capacity, uniqueness)
- [ ] Correct response format
- [ ] Correct HTTP status codes
- [ ] Data persisted to database

---

## 🔐 Security

### Current
- ✅ Password hashing (werkzeug)
- ✅ JWT authentication
- ✅ Role-based access control
- ✅ SQLAlchemy ORM (SQL injection prevention)

### Recommendations
- Upgrade to bcrypt/argon2
- Add JWT refresh tokens
- Input validation (marshmallow/pydantic)
- Rate limiting (Flask-Limiter)
- HTTPS in production
- Better error handling
- Logging & monitoring
- .env file for secrets

---

## 📚 Documentation & Resources

### Local Development Documentation
- **Swagger UI**: http://localhost:4000/apidocs
- **OpenAPI Spec**: http://localhost:4000/api/openapi.yaml

### Production Documentation & Links
- **Production API**: https://events-api-latest-rsgk.onrender.com
- **Production Health Check**: https://events-api-latest-rsgk.onrender.com/api/health
- **Production Swagger UI**: https://events-api-latest-rsgk.onrender.com/apidocs

---

## 🎯 Showcase Your Work

### ✨ Live Production Deployment

This project is fully deployed and running in production! Click the links below to see it in action:

#### 🌐 **Production API - Live on Render**
```
https://events-api-latest-rsgk.onrender.com
```

**What you can do:**
- ✅ Make API calls to the live endpoint
- ✅ Test all 17 endpoints in production
- ✅ View health status with Swagger UI
- ✅ Access interactive API documentation
- ✅ Download OpenAPI specification

**🎯 To Test the API with Swagger UI:**

1. **👉 [Open Swagger UI](https://events-api-latest-rsgk.onrender.com/apidocs)** ← Click here to get started!

2. **Select Production Server** (⚠️ Important!):
   - Look for **Servers** dropdown in Swagger UI
   - Choose: `https://events-api-latest-rsgk.onrender.com`
   - This ensures all test requests go to production

3. **Start Testing**:
   - Click any endpoint to expand
   - Click "Try it out"
   - Click "Execute"
   - See live responses!

**OpenAPI Server Configuration:**
```yaml
servers:
  - url: https://events-api-latest-rsgk.onrender.com
    description: Production server
  - url: http://localhost:4000
    description: Local development server
```

**Quick Test Examples:**
```bash
# Health Check
GET https://events-api-latest-rsgk.onrender.com/api/health
Response: { "status": "healthy" }

# List All Events
GET https://events-api-latest-rsgk.onrender.com/api/events
Response: Array of all events in production

# Register User (requires JSON body)
POST https://events-api-latest-rsgk.onrender.com/api/auth/register
Body: { "username": "testuser", "password": "TestPass123" }
```

---

#### 🐳 **Docker Image - Published on Docker Hub**
```
docker pull abhisakh/events-api:latest
```
**Repository Details:**
- ✅ Fully public Docker Hub repository
- ✅ Multiple image tags (latest, commit SHA, branch)
- ✅ linux/amd64 architecture for Render compatibility
- ✅ Automated builds via GitHub Actions

**👉 [View Docker Hub Repository](https://hub.docker.com/r/abhisakh/events-api)** ← See image details!

---

#### 💻 **Source Code - Open on GitHub**
```
github.com/abhisakh/events-api
```
**Repository Includes:**
- ✅ Complete source code
- ✅ Docker configuration (Dockerfile, docker-compose.yml)
- ✅ CI/CD pipeline (GitHub Actions v5)
- ✅ Complete test suite (17 tests)
- ✅ Comprehensive README documentation
- ✅ Automated deployment workflow

**👉 [View GitHub Repository](https://github.com/abhisakh/events-api)** ← Explore source code!

**CI/CD Pipeline Dashboard:**
👉 [View GitHub Actions Pipeline](https://github.com/abhisakh/events-api/actions) ← Monitor builds & deployments!

---

### 📊 Production Status Dashboard

| Component | Status | Link |
|-----------|--------|------|
| 🌐 **API Server** | ✅ Live & Running | [events-api-latest-rsgk.onrender.com](https://events-api-latest-rsgk.onrender.com) |
| 🐳 **Docker Image** | ✅ Published | [hub.docker.com/r/abhisakh/events-api](https://hub.docker.com/r/abhisakh/events-api) |
| 💻 **Source Code** | ✅ Open Source | [github.com/abhisakh/events-api](https://github.com/abhisakh/events-api) |
| 🔄 **CI/CD Pipeline** | ✅ Automated | [github.com/abhisakh/events-api/actions](https://github.com/abhisakh/events-api/actions) |
| 🔷 **Render Service** | ✅ Active | [dashboard.render.com](https://dashboard.render.com) → events-api-latest-rsgk |

---

### 🎓 What This Project Demonstrates

This production deployment showcases:

✅ **Full-Stack Development**
- Flask REST API development
- SQLAlchemy ORM with SQLite
- JWT authentication & authorization
- Role-based access control

✅ **DevOps & Containerization**
- Docker image creation
- Multi-platform architecture (linux/amd64)
- Docker Compose orchestration
- Container optimization & caching

✅ **CI/CD Automation**
- GitHub Actions v5 workflow
- Automated testing (17 tests)
- Automated building & pushing to Docker Hub
- Automated deployment to Render

✅ **Cloud Deployment**
- Render platform integration
- Webhook automation
- Automatic rollout & health checks
- Production monitoring & logs

✅ **Testing & Quality Assurance**
- Unit tests (test_models.py - 5 tests)
- Integration tests (test_api.py - 12 tests)
- Health checks in CI/CD pipeline
- Live smoke tests against production

✅ **Documentation**
- API documentation with Swagger UI
- OpenAPI 3.0 specification
- Comprehensive README (3,500+ lines)
- Inline code comments & explanations

---

**Made with ❤️ for learning DevOps, Cloud Deployment, and Modern Development Practices**
