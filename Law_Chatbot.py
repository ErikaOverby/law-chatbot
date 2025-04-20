# legal_bot.py

# Contract Law Chatbot – For Educational Use
# Author: Erika Overby
# License: MIT License (2025)

def intro():
    print("📚 Welcome to Law Chatbot – Contract Law Assistant")
    print("This chatbot provides general information about contract law.")
    print("It does not offer legal advice. For educational purposes only.\n")

def get_response(question):
    question = question.lower()

    responses = {
        ("offer", "offers"):
            "An offer is a clear expression of willingness to enter into an agreement under specific terms.",

        ("acceptance", "accept"):
            "Acceptance is the unqualified agreement to the terms of an offer, forming a binding contract.",

        ("consideration", "considerations"):
            "Consideration refers to something of value exchanged between the parties in a contract.",

        ("breach", "breaches"):
            "A breach of contract occurs when one party fails to fulfill their obligations under the agreement.",

        ("capacity", "capacities"):
            "Contractual capacity means a party has the legal ability to enter into a binding contract.",

        ("void", "voidable"):
            "A void contract has no legal effect; a voidable contract is valid but can be rescinded by one party.",

        ("remedy", "remedies"):
            "Common contract remedies include damages, specific performance, and rescission.",

        ("term", "terms", "contract", "contracts"):
            "Contract terms define the rights and duties of the parties. They can be express or implied.",

        ("elements", "components", "parts"):
            ("The essential parts of a valid contract typically include:\n"
             "- Offer\n"
             "- Acceptance\n"
             "- Consideration\n"
             "- Legal capacity\n"
             "- Lawful purpose\n"
             "- Mutual assent (meeting of the minds)"),
    }

    # Match based on any keyword found in the question
    for keywords, response in responses.items():
        if any(keyword in question for keyword in keywords):
            return response

    return ("I'm sorry, I can only answer basic contract law questions. "
            "Please ask about: offer, acceptance, consideration, breach, remedies, capacity, or contract terms.")

def run_chatbot():
    intro()
    while True:
        user_input = input("⚖️  Ask a contract law question (or type 'exit' to quit): ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("\nThank you for using Law Chatbot. Goodbye!")
            break
        response = get_response(user_input)
        print("📖 Bot:", response + "\n")

if __name__ == "__main__":
    run_chatbot()
