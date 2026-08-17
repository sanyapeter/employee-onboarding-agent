# Employee Onboarding AI Agent

## Architecture

The Employee Onboarding AI Agent helps employees get answers to onboarding questions and safely request actions. The agent uses a knowledge base, policy checks, and audit logging to ensure requests are handled securely.

```text
                         ┌───────────────┐
                         │    EMPLOYEE   │
                         │               │
                         │ Ask Question  │
                         │ / Request     │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │    main.py    │
                         │               │
                         │ Entry Point   │
                         └───────┬───────┘
                                 │
                                 ▼
                  ┌──────────────────────────┐
                  │    AI ONBOARDING AGENT   │
                  │                          │
                  │ Understand Intent        │
                  │ Decide What To Do        │
                  └────────────┬─────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐         ┌─────────────────┐
        │  KNOWLEDGE BASE │         │     ACTIONS     │
        │                 │         │                 │
        │ onboarding.json │         │   actions.py    │
        │ Company Info    │         │ Create Request  │
        │ Onboarding Info │         │ Perform Action  │
        └────────┬────────┘         └────────┬────────┘
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐         ┌─────────────────┐
        │     ANSWER      │         │  POLICY CHECK   │
        │                 │         │    policy.py    │
        │ Provide relevant│         │                 │
        │ information     │         │ Is it safe?     │
        └─────────────────┘         └────────┬────────┘
                                             │
                                  ┌───────────┴───────────┐
                                  │                       │
                                  ▼                       ▼
                           ┌────────────┐          ┌────────────┐
                           │    SAFE    │          │ SENSITIVE  │
                           └─────┬──────┘          └─────┬──────┘
                                 │                       │
                                 ▼                       ▼
                           ┌───────────┐          ┌────────────┐
                           │  EXECUTE  │          │  ESCALATE  │
                           │  ACTION   │          │  HR / IT   │
                           └─────┬─────┘          └────────────┘
                                 │
                                 ▼
                         ┌─────────────────┐
                         │     audit.py    │
                         │                 │
                         │ Log Decisions   │
                         │ & Actions       │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │    AUDIT LOG    │
                         │                 │
                         │ Traceability &  │
                         │ Accountability  │
                         └─────────────────┘
