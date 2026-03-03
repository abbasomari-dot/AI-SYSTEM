from app.business_orchestrator import BusinessOrchestrator


result = BusinessOrchestrator.run(
    lead_tier="high",
    core_problem="low_visibility",
    social_status="weak",
    rating=4.1,
    reviews=32
)

print("\n=== OFFER ===")
print(result.offer)

print("\n=== ANGLE ===")
print(result.angle)

print("\n=== PROPOSAL TITLE ===")
print(result.proposal.title)

print("\n=== COLD DM ===")
print(result.outreach.cold_dm)