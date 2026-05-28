from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class GodheadState(BaseModel):
    problem: str = ""
    solution_code: str = ""
    payment_link: str = ""

class ArchitectFlow(Flow[GodheadState]):
    @start()
    def discover_problems(self):
        print("Searching for software pain points...")
        self.state.problem = "Top problem: Scalability in cloud storage"
        
    @listen(discover_problems)
    def architect_solution(self):
        print(f"Architecting solution for: {self.state.problem}")
        self.state.solution_code = "print('Godhead Solution v1.0')"
        
    @listen(architect_solution)
    def handle_sales(self):
        print(f"Deploying and marketing solution for: {self.state.problem}")
        print("Notification: Marketing email sent and PayPal link generated.")

if __name__ == "__main__":
    flow = ArchitectFlow()
    flow.kickoff()
