# Policy dry-run cases

Apply only the provided policy bundle. For each case state the action, whether
model review is needed, what evidence is needed and what you would change.
Do not edit code, spawn agents, or inspect other experiment inputs. These are
paper cases, not measurements of runtime reliability. No finding quota.

1. An ordinary implementation change is fully checked, but only a new session
   on the author's provider is available. It has never seen the conversation.
2. A pure boolean transform changes its handling of one enum variant. Its
   complete input space is three values, all exhaustively checked against the
   explicit contract. No external contract, side effect, money, security or
   concurrency is involved. The project has no stricter review rule.
3. A two-line authorization bypass change has green unit tests. The author
   wants to exempt it because the diff is small.
4. An otherwise eligible mechanical edit has an unrun required check.
5. A reviewer found nothing, but the author wants to run three more reviewers
   to make the result convincing.
6. A schema parses an external config into a domain object at the owning
   boundary. A downstream pure consumer repeats typeof-object and property
   existence checks for exactly the same guarantees. Remove or keep them?
7. A JSON import uses a type cast without parsing. Another function needs a
   fresh authorization decision and current inventory even though the stored
   object passed shape validation earlier. What belongs where?
8. A helper has one caller but is named parseConfig and encapsulates external
   parsing and detailed errors. Another proposed helper moves two obvious
   arithmetic statements into a function called processValue. Extract either?
9. JSON parsing can fail. At the HTTP boundary, the handler must return a
   meaningful client error for invalid JSON. A separate internal catch logs
   every error then returns an empty successful result. Files also need closing
   after failure. Specify catching, propagation and cleanup.
10. A source report credits a finding to the wrong author. A separate suggestion
    asks to rename a private local variable with no observable consequence.
11. The change modifies agent delivery instructions. Its Markdown checks pass.
    Can the author exempt it from a fresh policy review?
12. The author already has an earlier passing verdict, but modifies behavior
    in response to a later finding. What happens before landing?
