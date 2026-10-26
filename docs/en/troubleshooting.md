# Troubleshooting

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| It answers with **work** instead of questions | The letter did not load (too long, wrong field, parent file overriding it) or the model skipped the protocol | Check you pasted into the field that applies to every conversation; check the [platform page](platforms/README.md) for size limits; if needed paste the letter as the first message and ask: "Run your first-boot protocol before anything else." |
| It **invents a personality** or a name | It filled in blanks instead of asking | Say: "You don't have a name or role yet. Ask me." If it persists, the letter is not loading in full. |
| It starts **creating agents** | The model read a manual-style text as its job | You may have pasted something other than the letter. The letter explicitly says the agent is not a creator. Re-paste the letter alone in a fresh conversation. |
| It asks for **passwords or keys** | Breaking the secrets rule | Never provide them. Add the failure to your tests; correct the SOUL; retest. |
| It says it has **tools it doesn't have** | Guessing | Ask it to list exactly what it can do; compare with your configuration; correct question 4's answer. |
| It **forgets who it is** next conversation | The SOUL was not saved where the platform reloads it | Follow the "Where the SOUL lives" section of your [platform page](platforms/README.md). |
| It **acts without confirmation** | The platform allows it and the rule was not followed | Treat as a failed boundary test: tighten permissions first (read-only), then correct the SOUL and retest before using it. |
| The letter **does not fit** the field | Platform length limit | Use the pointer-plus-file fallback on your platform page, and verify in the first reply. |
| **Different models behave differently** | Models follow long instructions with different fidelity | Re-run the first-boot check and the rule tests with the model you actually use. |

## If nothing works

Start a fresh conversation with **only** the letter, nothing else in the context, and compare. Many problems come from other instructions or files that sit around the letter.

Found a gap in these pages or in the letters? Open an issue describing the platform, the model and what you saw.
