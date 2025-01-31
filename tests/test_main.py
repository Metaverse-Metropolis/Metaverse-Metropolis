# Test Main Application

This file contains unit tests for the main application of the Metaverse Metropolis AI Agent.

## Example Test Code

```python
import unittest
from src.main import AI_Agent

class TestAI_Agent(unittest.TestCase):

    def test_initial_status(self):
        agent = AI_Agent()
        self.assertEqual(agent.get_status()["status"], "inactive")

    def test_activate_agent(self):
        agent = AI_Agent()
        agent.activate()
        self.assertEqual(agent.get_status()["status"], "active")

    def test_deactivate_agent(self):
        agent = AI_Agent()
        agent.activate()
        agent.deactivate()
        self.assertEqual(agent.get_status()["status"], "inactive")

if __name__ == '__main__':
    unittest.main()
