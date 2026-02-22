# Module 04: Domain Concepts Cheat Sheet 🧠

> These are system design terms you'll see in task tickets.
> You don't need to memorize them — just know what they mean
> so you're not confused when you see them in Week 2+.

---

## Concepts You'll Encounter

### 🚦 Rate Limiter
**What it is:** Controls how many requests a user can make per time period.

**Real-world analogy:** A bouncer at a club — "Only 100 people per hour."

**How it works:**
```
Client sends request → Rate limiter checks: "Has this IP sent too many?"
  ├── Under limit → Allow request through
  └── Over limit  → Return "429 Too Many Requests" with Retry-After header
```

**Where you'll see it:** Week 1 (Task 4)

---

### 🏊 Connection Pool
**What it is:** A collection of reusable database connections, shared across requests.

**Real-world analogy:** A car rental company — instead of buying a car for each
customer, they rent cars from a pool and return them when done.

**How it works:**
```
Request needs DB connection → Pool checks: "Any available connections?"
  ├── Available → Give the connection, mark it as "in use"
  ├── All busy  → Wait in queue until one is returned
  └── Connection too old → Create a fresh one
```

**Where you'll see it:** Week 1 (Task 5)

---

### 📋 Task Scheduler / Priority Queue
**What it is:** A system that runs tasks in priority order, not FIFO order.

**Real-world analogy:** Hospital ER — a heart attack patient is treated before
a sprained ankle, even if the sprain arrived first.

**How it works:**
```
Tasks arrive: [low, critical, medium, high]
Queue orders: [critical, high, medium, low]  ← highest priority first
```

**Where you'll see it:** Week 1 (Task 3)

---

### 🔄 Pipeline / ETL
**What it is:** A data processing chain — Extract → Transform → Load.

**Real-world analogy:** A factory assembly line — raw materials come in,
each station modifies them, and finished products come out.

**How it works:**
```
Raw Data → [Validate] → [Transform] → [Enrich] → [Load to DB]
               ↓              ↓
          Bad records    Failed transforms
          go to DLQ      go to DLQ
```

**Where you'll see it:** Week 3 (Tasks 3-4)

---

### 💀 Dead Letter Queue (DLQ)
**What it is:** A holding area for messages/records that failed processing.

**Real-world analogy:** The "undeliverable mail" bin at the post office.

**How it works:**
```
Record fails processing → Retry 3 times
  ├── Succeeds on retry → Continue
  └── All retries fail  → Move to Dead Letter Queue for manual review
```

**Where you'll see it:** Week 3 (Task 4)

---

### 💾 Cache
**What it is:** Fast temporary storage to avoid expensive operations.

**Real-world analogy:** A sticky note on your desk with a frequently-used
phone number — faster than looking it up in the directory every time.

**How it works:**
```
Request for data → Check cache first
  ├── Cache HIT  → Return cached data (fast!)
  └── Cache MISS → Fetch from database (slow), store in cache for next time
```

**Cache invalidation** (when to remove old data) is famously one of the
two hardest problems in computer science.

**Where you'll see it:** Week 2, Week 4

---

### 🔌 API Middleware
**What it is:** Code that runs BEFORE your main handler — like a security guard
checking IDs before letting you into the building.

**Real-world analogy:** Airport security — every passenger goes through
the same screening before reaching their gate.

**How it works:**
```
Request → [Auth Middleware] → [Rate Limiter] → [Logger] → [Your Handler]
              "Who are you?"     "Too many?"     "Log it"     "Process it"
```

**Where you'll see it:** Week 1 (Tasks 4, 6), Week 2

---

### 📨 Message Queue
**What it is:** A buffer between services — one sends messages, another processes them
at its own pace.

**Real-world analogy:** A restaurant order queue — the waiter puts orders on a
ticket rail, and the chef picks them up when ready.

**How it works:**
```
Producer → [Queue: msg1, msg2, msg3] → Consumer
  "Send notification"                    "Process and send email"
```

**Key benefit:** The producer doesn't wait for the consumer to finish.

**Where you'll see it:** Week 3, Week 5

---

### 🔒 Circuit Breaker
**What it is:** A pattern that stops calling a failing service to prevent
cascading failures.

**Real-world analogy:** An electrical circuit breaker — when too much
current flows, it trips to prevent a fire.

**How it works:**
```
State: CLOSED (normal)
  Requests go through normally
  If 5 failures in a row → switch to OPEN

State: OPEN (protecting)
  All requests immediately fail (don't even try)
  After 30 seconds → switch to HALF-OPEN

State: HALF-OPEN (testing)
  Allow ONE request through
  If it succeeds → back to CLOSED
  If it fails → back to OPEN
```

**Where you'll see it:** Week 4, Week 6

---

### 🌳 Dependency Resolver (Topological Sort)
**What it is:** Figures out the correct order to do things when tasks
depend on each other.

**Real-world analogy:** Getting dressed — you can't put on shoes before
socks, and you can't put on a shirt before... well, you can, but the
point is some things depend on others.

**How it works:**
```
Dependencies:
  A depends on B, C
  B depends on D
  C depends on D

Correct order: D → B → C → A  (or D → C → B → A)
```

**The bug to watch for:** Circular dependencies (A needs B, B needs A).
This should be detected and reported, not cause an infinite loop.

**Where you'll see it:** Week 7 (Task 3)

---

### 📊 Monitoring & Alerting
**What it is:** Watching your system's health and notifying when things go wrong.

**Real-world analogy:** The dashboard in your car — speedometer, fuel gauge,
temperature warning light.

**Key metrics:**
- **Latency** — How long requests take (target: <200ms)
- **Error rate** — % of requests that fail (target: <1%)
- **Throughput** — Requests per second (target: depends on system)
- **Uptime** — % of time the system is available (target: 99.9%)

**Where you'll see it:** Week 5, Week 6

---

### 🗄️ Database Migration
**What it is:** Changing your database structure (adding tables, columns, etc.)
in a controlled, reversible way.

**Real-world analogy:** Renovating a building while people are still living
in it — you can't just tear down walls randomly.

**How it works:**
```
Migration 001: Create users table
Migration 002: Add email column to users
Migration 003: Create orders table

Each migration can be:
  - Applied (upgrade) — make the change
  - Rolled back (downgrade) — undo the change
```

**Where you'll see it:** Week 8

---

## Week 5-8 Concepts

### 🏴 Feature Flags
**What it is:** A way to turn features on/off without deploying new code.

**Real-world analogy:** A light switch — you can turn a room's lights on for some people
and off for others, without rewiring the building.

**How it works:**
```
User request → Check feature flag for this user
  ├── Flag ON  → Show new feature
  └── Flag OFF → Show old behavior
```

**Why it matters:** Companies roll out features gradually — first to 1% of users,
then 10%, then 100%. If something breaks, just flip the flag off.

**Where you'll see it:** Week 7 (Task 5)

---

### 📡 Distributed Tracing
**What it is:** Following a single user request as it travels through multiple services.

**Real-world analogy:** A package tracking number — you can see every warehouse
your package passed through, how long it spent at each one.

**How it works:**
```
Request arrives → Assign Trace ID: "abc-123"
  → Service A (50ms) [trace: abc-123, span: 1]
    → Service B (30ms) [trace: abc-123, span: 2]
    → Database (20ms) [trace: abc-123, span: 3]
```

Every service logs the same Trace ID, so you can reconstruct the full journey.

**Where you'll see it:** Week 5 (Task 5)

---

### 🔵🟢 Blue-Green Deployment
**What it is:** Running two identical environments — "blue" (current) and "green" (new).
You switch traffic from blue to green when the new version is ready.

**Real-world analogy:** A restaurant with two identical kitchens. You prep the new
menu in Kitchen B while Kitchen A serves customers. When ready, switch all orders to Kitchen B.

**How it works:**
```
Blue (v1.0) ← ALL traffic
Green (v2.0) ← No traffic (being tested)

Ready? Flip the switch:

Blue (v1.0) ← No traffic (standby)
Green (v2.0) ← ALL traffic

Something wrong? Flip back instantly.
```

**Where you'll see it:** Week 7 (Task 4)

---

### 🐤 Canary Release
**What it is:** Sending a small percentage of traffic to the new version first,
then gradually increasing if metrics look good.

**Real-world analogy:** "Canary in a coal mine" — miners sent a canary bird down
first. If the bird was fine, the air was safe. Same idea with software.

**How it works:**
```
v1.0 ← 95% of traffic
v2.0 ← 5% of traffic (the "canary")

Monitor for 30 minutes...
  ├── Error rate OK → Increase to 25%, then 50%, then 100%
  └── Error rate high → Roll back canary to 0%
```

**Where you'll see it:** Week 7 (Task 6)

---

### 🛡️ Load Shedding
**What it is:** Intentionally dropping low-priority requests when the system is overloaded,
to protect high-priority requests.

**Real-world analogy:** During a power shortage, the power company cuts electricity
to non-essential areas to keep hospitals and emergency services running.

**How it works:**
```
System load at 90% → Admit all requests
System load at 95% → Reject low-priority requests
System load at 99% → Reject everything except critical
```

**Where you'll see it:** Week 8 (Task 6)

---

### 🛑 Graceful Shutdown
**What it is:** Stopping a service cleanly — finish all in-progress requests,
close database connections, flush logs — before actually shutting down.

**Real-world analogy:** A store that announces "We're closing in 15 minutes"
instead of just locking the doors with customers still inside.

**How it works:**
```
Shutdown signal received:
  1. Stop accepting NEW requests
  2. Wait for in-progress requests to finish (with timeout)
  3. Close database connections
  4. Flush log buffers
  5. Exit cleanly
```

**Where you'll see it:** Week 8 (Task 3)

---

### 🔒 PII Masking
**What it is:** Replacing personally identifiable information (emails, phone numbers,
SSNs) with masked versions before storing or displaying.

**Real-world analogy:** A redacted document where sensitive parts are blacked out:
"The patient ████████ was treated at ████████ Hospital."

**How it works:**
```
Input:  {"name": "John Doe", "email": "john@gmail.com", "ssn": "123-45-6789"}
Output: {"name": "J*** D**", "email": "j***@g****.com", "ssn": "***-**-6789"}
```

**Why it matters:** GDPR, HIPAA, and other laws REQUIRE companies to protect personal data.
Getting this wrong can result in millions in fines.

**Where you'll see it:** Week 6 (Task 3)

---

### 📊 SLA / SLO
**What it is:**
- **SLA** (Service Level Agreement) — A contract with customers: "Our service will be
  available 99.9% of the time."
- **SLO** (Service Level Objective) — Internal targets that are stricter than the SLA:
  "We aim for 99.95% to have a safety margin."

**Real-world analogy:** An airline promises flights arrive within 30 minutes of
scheduled time (SLA). Internally, they aim for 15 minutes (SLO).

**Key metrics:**
```
Availability SLA: 99.9% → Only 8.7 hours of downtime allowed per year
Latency SLO: p99 < 500ms → 99% of requests must respond within 500ms
Error Rate SLO: < 1% → Less than 1 in 100 requests can fail
```

**Where you'll see it:** Week 8 (Task 6)

---

### 💳 Payment Reconciliation
**What it is:** Matching your internal records against the payment gateway's records
to make sure every transaction is accounted for.

**Real-world analogy:** Balancing your checkbook — comparing your spending notes
with your bank statement to make sure nothing is missing or duplicated.

**How it works:**
```
Our records: [Order #101: $50, Order #102: $30, Order #103: $75]
Gateway records: [Txn A: $50, Txn B: $30, Txn C: $75]

Match them → Are all amounts correct? Any missing? Any duplicates?
```

**Where you'll see it:** Week 5 (Task 3, Service Track)

---

### 🔢 API Versioning
**What it is:** Running multiple versions of an API simultaneously so old clients
don't break when you release new features.

**Real-world analogy:** A menu that says "Classic Burger (original recipe)" and
"New Burger (2026 recipe)" — old customers can still order what they're used to.

**How it works:**
```
GET /api/v1/users → Returns {name, email}
GET /api/v2/users → Returns {name, email, avatar, preferences}

v1 is deprecated but still works for 6 months.
```

**Where you'll see it:** Week 8 (Task 5)

---

### 📄 Cursor-Based Pagination
**What it is:** Fetching large datasets in pages using a cursor (bookmark) instead
of page numbers.

**Real-world analogy:** Instead of saying "give me page 5 of results," you say
"give me 20 results starting after THIS item."

**How it works:**
```
Request: GET /items?limit=20&cursor=abc123
Response: {
  items: [...20 items...],
  next_cursor: "def456"  ← Use this for the next page
}
```

**Why cursor > offset:** If new items are inserted between pages, offset-based
pagination can show duplicates or skip items. Cursors don't have this problem.

**Where you'll see it:** Week 7 (Task 7, Service Track)

---

### 🔑 Session Management
**What it is:** Tracking who is logged in, ensuring sessions expire after inactivity,
and allowing users to log out of all devices.

**Real-world analogy:** A visitor badge at an office building — it records when you
entered, expires after 8 hours, and security can revoke it if needed.

**How it works:**
```
Login → Create session token (random, unique)
  → Store: {token: "abc", userId: 42, expiresAt: "2026-03-15T18:00:00"}
  → Set cookie on client

Each request → Validate token → Is it expired? Revoked?
  ├── Valid → Allow request, renew expiry
  └── Invalid → 401 Unauthorized
```

**Where you'll see it:** Week 6 (Task 5, Service Track)

---

### 📜 Log Rotation
**What it is:** Automatically archiving old log files and creating new ones
to prevent disks from filling up.

**Real-world analogy:** Replacing a full notebook with a new one, and filing
the old one on a shelf. After 90 days, shred the oldest notebooks.

**How it works:**
```
app.log reaches 100MB:
  1. Rename app.log → app.log.2026-03-15.gz (compressed)
  2. Create new empty app.log
  3. Delete archives older than 90 days
```

**Where you'll see it:** Week 7 (Task 4, Service Track)

---

## Quick Reference Card

| Concept | One-Line Definition | Week |
|---------|-------------------|------|
| Rate Limiter | Limits requests per time period | W1 |
| Connection Pool | Reusable database connections | W1 |
| Priority Queue | Tasks ordered by importance | W1 |
| Pipeline/ETL | Chain of data processing steps | W3 |
| Dead Letter Queue | Storage for failed messages | W3 |
| Cache | Fast temporary data storage | W2, W4 |
| Middleware | Code that runs before every request | W1, W2 |
| Message Queue | Buffer between services | W3, W5 |
| Circuit Breaker | Stops calling failing services | W4, W6 |
| Dependency Resolver | Orders tasks by dependencies | W7 |
| Monitoring | Watches system health metrics | W5, W6 |
| DB Migration | Controlled database changes | W8 |
| Feature Flags | Toggle features on/off without deploy | W7 |
| Distributed Tracing | Track requests across services | W5 |
| Blue-Green Deploy | Two environments, instant switch | W7 |
| Canary Release | Gradual traffic shift to new version | W7 |
| Load Shedding | Drop low-priority requests under load | W8 |
| Graceful Shutdown | Clean service stop (finish work first) | W8 |
| PII Masking | Hide personal data in records | W6 |
| SLA / SLO | Service reliability contracts/targets | W8 |
| Payment Reconciliation | Match internal vs external records | W5 |
| API Versioning | Multiple API versions simultaneously | W8 |
| Cursor Pagination | Bookmark-based page navigation | W7 |
| Session Management | Track logins, expiry, revocation | W6 |
| Log Rotation | Archive old logs, prevent disk full | W7 |
