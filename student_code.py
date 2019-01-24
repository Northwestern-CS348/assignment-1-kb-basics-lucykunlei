import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        """check if the argument is a fact"""
        print("Asserting {!r}".format(fact))
        if isinstance(fact, Fact):
            """if true, check if the argument is already in the KB as a fact"""
            if fact in self.facts:
                print('The argument', fact, 'already exists in the KB as a fact.')
                """if the argument does not exist in the KB.facts, then add it to the fact list"""
            else: 
                self.facts.append(fact)
                """Mark this fact as asserted"""
                fact.asserted = True
                """print success message"""
                print("Argument {!r}".format(fact), 'successfully added to KB as a fact.')
        elif isinstance(fact, Rule):
            """if true, check if the arugment is already in the KB as a rule"""
            if fact in self.rules:
                print('The argument', fact, 'already exists in the KB as a rule.')
            else: 
                self.rules.append(fact)
                fact.asserted = True
                print("Argument {!r}".format(fact), 'successfully added to KB as a rule.')
        else: print('The argument', fact, 'is neither a fact nor a rule; cannot be added to the KB.')
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))

        if not isinstance(fact, Fact):
            print("The argument asking for is not a fact.")
            return False
        elif not self.facts: 
            print("There is no facts in the KB.")
            return False
        else:
            result_binding_list = ListOfBindings()
            for existingFact in self.facts:
                if not match(fact.statement, existingFact.statement):
                    continue
                else: result_binding_list.add_bindings(match(fact.statement,existingFact.statement))
            if len(result_binding_list)==0:
                return False
            else:
                return result_binding_list










            
