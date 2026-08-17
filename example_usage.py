from client import MultiAgentDebateConsensusArbitrationClient

def main():
    client = MultiAgentDebateConsensusArbitrationClient()
    agents = ["ArchitectAgent", "SecurityAgent", "PerformanceAgent"]
    res = client.arbitrate_debate("Synchronous RPC vs Message Queues for Agent Fleet", agents)
    print(f"Confidence: {res['agreement_confidence_pct']}%")
    print(f"Dissenting Views Resolved: {res['dissenting_views_resolved']}")
    print(f"Consensus: {res['consensus_verdict']}")

if __name__ == "__main__":
    main()
