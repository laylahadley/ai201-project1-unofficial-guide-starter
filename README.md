# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
     Domain: Internship and Recruiting Knowledge for Howard University Finance and Business Students

     Domain Value: - For finance and business students at Howard University, securing highly coveted internships (particularly in investment banking, corporate finance, and consulting) requires more than just a high GPA. The recruiting timeline for Wall Street and top business firms is notoriously accelerated and highly competitive. This domain provides the tactical "playbook" for success by synthesizing both formal institutional resources and informal student networks.
          - targeted interview prep
          - relevant extracurriculars
          - mentorship
          - networking methods
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

---
| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 |reddit |Howard v. American |https://www.reddit.com/r/HowardUniversity/comments/1bo7x3i/howard_v_american_and_other_dc_area_schools/|
| 2 |Black Enterprise |Howard Finance Career Pipeline |https://www.blackenterprise.com/howard-university-graduates-finance-careers/ |
| 3 |Howard SOB Website |Student Forum |https://business.howard.edu/centers/hps-center-financial-excellence/students |
| 4 |The Dig - HU News |Howard to WallStreet Pipeline |https://thedig.howard.edu/all-stories/mecca-wall-street-howards-hps-center-shaping-future-finance |
| 5 |Plexxus |Howard Finance Career Pipeline |https://plexuss.com/f3/howard-university-internship-opportunities-for-students |
| 6 |Howard Forum |Howard Career Pipeline |https://business.howard.edu/sites/business.howard.edu/files/2022-05/2022-2023%20HUSB%20Recruitment%20Guide%20.pdf |
| 7 |Reddit |Helpful Info for incoming freshman |https://www.reddit.com/r/HowardUniversity/comments/1c6h31d/what_should_incoming_howard_students_know/ |
| 8 |HBCU Connect |Wells Fargo HBCU Recruitment |https://hbcuconnect.com/content/401535/wells-fargo-hosts-interactive-info-session-for-howard-university-students-explore-careers-in-corporate-investment-banking |
| 9 |HPS Center for Finance |Center for Financial Excellence |https://business.howard.edu/centers/hps-center-financial-excellence |
| 10 |Rate my Professor |HU Finance Professors |https://www.ratemyprofessors.com/search/professors/421?q=*&did=21 |


## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 
     - 200 (tokens)

**Overlap:** 
     - 30 (tokens)

**Why these choices fit your documents:**
     - My corpus mixes two very different document types: short, multi-subject pages (e.g., a RateMyProfessors-style page covering 12 different professors in one file) and longer single-topic articles (e.g., news coverage of Howard's HPS Center for Financial Excellence). I originally chunked at 500 tokens, but testing retrieval against a real query ("which professors are known to be strong mentors") revealed that 500-token chunks were merging 3+ unrelated professors' reviews into a single chunk, diluting the embedding and preventing any single professor's review from being retrieved distinctly, a query about mentorship returned only institutional program content, with the top result scoring 0.544, well above the 0.5 relevance threshold, and no professor names appearing anywhere in the top 5. I reduced chunk size to 200 tokens with 30-token overlap so that review-style content splits closer to one professor per chunk, while longer narrative articles simply span more chunks rather than losing coherence. After this change, the same RateMyProfessors document split from 4 chunks to 9 (closer to, though not exactly, one chunk per professor. a few professors' reviews are still short enough to share a chunk), and the same mentorship query correctly surfaced a specific professor 
(Dr. Denise Streeter) with source attribution. The 30-token overlap preserves continuity for sentences that span a chunk boundary without being large enough to reintroduce the original dilution problem.

**Final chunk count:** 
     - 51



---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

| # | Source document | Chunk text |
|---|----------------|------------|
| 1 |[Source: blackenterprise_howard_finance_careers.txt | Chunk 0] |Howard University Steps Up To Place Its Graduates In Lucrative Finance Careers
Mentorship, practical experience and a supportive networking community are among resources graduates from Howard University contain as they enter the business world.

The HPS Center for Financial Excellence (HPS-CFE) at the Howard University School of Business has a lofty goal: Become a major player in positioning its graduates in the potentially lucrative financial services industry.

The HBCU aims to be viewed in the same light as other powerhouse business schools by helping to secure above-average finance roles for its graduates within the next four to five years. That is a desire for Curtis Kidd Telemaque, Ph.D., and director of HPS-CFE.

“The HPS Center was created to intentionally correct the skew from back office only positions to client-facing roles that require a highly technical skillset. As such, the center’s strategy has been to merge theoretical financial concepts taught in class with practitioner-led extra-curricular modules.”

LOCATING STUDENTS IN ROLES THEY HAVE BEEN NEGLECTED FROM

The Washington, D.C.-based school is boosting efforts to help HBCU students land future careers in investment banking, alternative finance, and asset management. Black students, especially those from HBCUs, have long not been equally represented in such high-paying roles.

Research shows that graduate hiring at global banks, like those based in New York, has just 0.5% of senior investment bankers who are Black. Another report reveals that minority- and women-owned firms manage just 1.4% of the roughly $82 trillion in U.S. assets under management, despite performing on par with industry averages.

Now, Howard‘s business school wants to help change these statistics.

SCORING HIGH-PAYING JOBS NEAR TIMES SQUARE AFTER GRADUATION

Helping change the narrative are Dylan Thomas and Jessica Barnes. They are now earning or about to earn “six-figure” salaries working at mega companies near Times Square in New York City.

After completing an internship at Barclays last summer, Thomas joined one of Wall Street’s most influential investment banks. He was just hired as an investment banking analyst at Barclays, stating his pay is “definitely more than I have ever made.”

“Essentially, if a tech media or telecommunications company finds itself in debt, they call my team, we lend them some money, and then we charge them for that money that they borrowed,” Thomas told BLACK ENTERPRISE.

He says HPS |
| 2 | blackenterprise_howard_finance_careers.txt | Chunk 1 |“Essentially, if a tech media or telecommunications company finds itself in debt, they call my team, we lend them some money, and then we charge them for that money that they borrowed,” Thomas told BLACK ENTERPRISE.

He says HPS-CFE supplied him with mentorship, exposure, and experience to help find his footing in the financial services industry.

Thomas reflected on how current and future students can benefit from a $10 million gift announced in 2021 by HPS Investment Partners and The Kapnick Foundation to create the HPS-CFE. You can learn more about the center and investment here. The project remains in progress, as Dr. Curtis Kidd Telemaque, who became the HPS-CFE director in 2021, continues to work with students.

The young analyst shared how the gift could help reduce the recognized disparity between blacks and whites, as well as others working in the industry. “HPS Investment Partners wants to do their part to take some of that load off us and to invest in our learning and our growth, said Thomas.”

He added, “Any young black professional aspiring to a career in financial services should seriously consider the value in the HPS-CFE as it is.”

Thomas and Barnes are among the first members of the graduating cohort of 13, receiving their degrees in May 2025 from Howard. Ten of those individuals have since secured high-finance employment roles in financial services and management consulting.

Barnes, 22, will begin working full-time this October as an enterprise strategy and value associate at Strategy&, the global consulting arm of accounting giant PricewaterhouseCoopers. Her job: Helping power utility and aerospace companies create strategies for sustaining growth, reshaping costs and business structures, along with integrating IT and digital operations. She will start her new role after completing three corporate internships.

GAINING THE RESOURCES TO FLOURISH IN THE HIGH-FINANCE SPACE

Barnes says CFE helped enhance her new career journey in many ways. For one, she developed some skills she will truly need professionally. And she says she founded the Howard University Women In Finance Initiative. The community largely connects Black women in the high finance sector.

“It gives women the power of representation and community to achieve their goals in a space that predominantly doesn’t have Black women.”

She added that the CFE gave her courage to take on the world. “We really got the backing to just feel like we are equipped with the skills and |
| 3 | blackenterprise_howard_finance_careers.txt | Chunk 2 |representation and community to achieve their goals in a space that predominantly doesn’t have Black women.”

She added that the CFE gave her courage to take on the world. “We really got the backing to just feel like we are equipped with the skills and resources that maybe even if you don’t have the answer now, I know I can rely on the network that I was given to get it.”

Students from CFE have secured jobs with several high-finance companies, including Partners Capital, Bank of New York Mellon, Barclays, Goldman Sachs, PwC, Vanguard, EY Parthenon, Carlyle, Union Bank of Switzerland, Truist, and MasterCard.

Kidd Telemaque added that, generally, they have landed high-paying positions immediately after graduation, with an average starting salary for the most recent cohort at $89K and approximately $10K in bonuses.

WORKING WITH BLUE-CHIP COMPANIES TO MAKE A DIFFERENCE

Additionally, HPS-CFE is stepping up efforts to boost the low representation of HBCU graduates in high finance. The center partners with a broad range of firms that offer a wide range of services, including private credit management, investment banking, and asset management, to facilitate change.

Kidd Telemaque says the firms include HPS Investment Partners, Vanguard, CFI, Goldman Sachs, and Warburg Pincus. “Our position is that companies are able to directly assess talent when they provide instruction or are otherwise involved in enhancing students’ practical finance skills.”

While disparities are not new to HBCUs, they have led to an outpouring of support for certain HBCUs to attract high-performing talent. “Due to this support, we can not only expose our students to all areas of finance but also provide practical, hands-on expertise before graduation.”

Still, actions to help uplift graduates are not obstacle-free. Kidd Telemaque says one of the center’s challenges is overcoming industry perception of HBCU graduates as being less qualified.

The HPS-CFE’s future ambition to place more HBCU graduates in elevated finance roles stems from the recent success of five Howard students, who won a $1 million grant for the school after winning the fifth annual Goldman Sachs Market Madness competition. It was disclosed that the money will be invested in infrastructure and academic programming for the university.

An HPS-CFE participant, Barnes offered some advice to existing students or those considering attending the center.

“Knowledge is power. “ |
| 4 | blackenterprise_howard_finance_careers.txt | Chunk 3 |Sachs Market Madness competition. It was disclosed that the money will be invested in infrastructure and academic programming for the university.

An HPS-CFE participant, Barnes offered some advice to existing students or those considering attending the center.

“Knowledge is power. “Learn what you don’t know and then strive to be excellent. I think that sometimes it’s so rare.” |
| 5 | hbcuconnect_wells_fargo_howard_info_session.txt | Chunk 0 |Wells Fargo Hosts Interactive Info Session for Howard University Students — Explore Careers in Corporate & Investment Banking

Washington, D.C. — Wells Fargo is inviting Howard University students to join an exciting, in-person Interactive Information Session focused on careers in Corporate & Investment Banking (CIB).

At Wells Fargo, education and opportunity go hand in hand. This engaging event, hosted by the Corporate & Investment Banking and Early Careers teams, is designed to give students a behind-the-scenes look at the world of finance while helping them prepare for future career success.

What to Expect
Gain insight into careers in finance and corporate banking
Learn about Wells Fargo’s culture, mission, and values
Network directly with Wells Fargo professionals
Hear exclusive tips from recruiters and program managers on how to stand out during the hiring process
Whether you’re exploring your career path or ready to take the next step, this session offers a valuable opportunity to connect, learn, and grow.

Event Details
Date: Thursday, October 29th
Time: 6:00 PM – 8:00 PM EST
Location: Howard University School of Business Auditorium
Attire: Business Professional
🍽️ Dinner will be provided, and all classes and majors are welcome!

Additional opportunities for coffee chats will be shared with registered participants.

How to Register
Students are encouraged to register by October 27th using the link below: |

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
     - all-MiniLM-L6-v2 (via sentence-transformers)

**Production tradeoff reflection:**
     - I chose all-MiniLM-L6-v2 because it runs entirely locally with no API key, no per-query cost, and no rate limits — well suited for a student project with a small, fixed corpus (51 chunks). It's also fast: embedding all chunks took under a second on a standard laptop.
     - If I were deploying this for real users without cost as a constraint, I'd weigh several tradeoffs before switching models:
          - **Context length:** all-MiniLM-L6-v2 has a relatively short max sequence length (256 tokens), which is part of why I kept my chunk size at 200 tokens rather than larger, content beyond the model's limit gets truncated silently. A model with a longer context window (e.g., OpenAI's text-embedding-3-large, or a larger local model) would let me use bigger chunks without losing information, which could better preserve long-form documents like the HUSB recruitment guide.
          - **Accuracy on domain-specific text:** all-MiniLM-L6-v2 is a general-purpose model. My domain includes informal, slang-heavy language (Reddit posts, student reviews) alongside formal institutional writing (recruitment guides). A larger or fine-tuned model might better bridge the vocabulary gap I saw in testing, for example, a query using "mentor" failing to match review language like "engaging lectures" or "offers extra credit."
          - **Latency and local vs. API-hosted:** Local inference avoids network latency and API costs entirely, which matters at scale with many concurrent users. But a hosted model offloads compute and typically receives more frequent updates/improvements than a static local model I'd have to manually re-download and redeploy.


---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:** 
     - "What resources does the HPS Center for Financial Excellence provide for Wall Street recruiting?"

Top returned chunks:
- husb_hps_center_financial_excellence.txt (distance: 0.300) - states the CFE's purpose: producing high-caliber graduates for investment/wealth management, banking, real estate, and capital markets careers
- husb_hps_center_students.txt (distance: 0.302) - lists concrete programs: Investment Management Academy Scholars Program, Wealth Management Program, Wall Street on Campus seminar, interview/resume bootcamps, Bloomberg terminal training, HPS mentorship program
- thedig_mecca_wall_street_hps_center.txt (distance: 0.373) - describes CFE's founding, leadership, and its "Wall Street on Campus" seminar bringing in Goldman Sachs, Morgan Stanley, Citi, and BNP Paribas

Relevance explanation:
     - All three chunks are highly relevant and well below the 0.5 distance threshold. The top two results come directly from documents purpose-built to describe the HPS Center's offerings, and both name specific, concrete programs rather than vague descriptions. This is a strong example of retrieval working as intended — the query's key terms ("resources," "HPS Center," "Wall Street") closely match the vocabulary used in the source documents themselves.
---

**Query 2:**
     - "What specific divisions of corporate and investment banking recruit at Howard from the Wells Fargo info session?" 

Top returned chunks:
- hbcuconnect_wells_fargo_howard_info_session.txt (distance: 0.207) - the article describing Wells Fargo's Corporate & Investment Banking (CIB) info session at Howard
- thedig_mecca_wall_street_hps_center.txt (distance: 0.415) - Howard's broader ambition to be known for financial teaching, likened to MIT/Columbia/Harvard 
- husb_recruitment_guide_2022_2023.txt (distance: 0.482) - general employer recruitment policies at Howard's Center for Career Excellence

Relevance explanation:
     - The top result is the strongest match of any query I tested (0.207) and correctly identifies the exact source document. However, this is also my documented failure case: the retrieved chunk only names a single umbrella group ("Corporate & Investment Banking") rather than the multiple specific sub-divisions my question assumed existed. Retrieval succeeded at finding the right document, but the underlying source content wasn't as detailed as my evaluation question expected - see Failure Case Analysis below.


---

**Query 3:**
     - "What is the exact timeline for finance and business recruiting according to the HUSB guide, and what are the formal steps to prepare my application?"
Top returned chunks:
- husb_hps_center_students.txt (distance: 0.519) — lists CFE bootcamps and career support offerings
- husb_hps_center_students.txt (distance: 0.521) — describes CFE experiential learning programs
- blackenterprise_howard_finance_careers.txt (distance: 0.567) — profile of a CFE graduate's career outcome


Relevance explanation:
     - This query failed to retrieve anything below the 0.5 distance threshold, all 5 results scored between 0.519 and 0.573. Notably, husb_recruitment_guide_2022_2023.txt (the document my question explicitly asked about) never appeared in the top 5 at all, despite being 11 chunks in my corpus. On inspection, that document is writtenfrom an employer's perspective (registration steps, job posting policies) rather than a student's, so it never actually contains a "student timeline", meaning even perfect retrieval likely couldn't have surfaced an answer that doesn't exist in the source material.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
     - The system prompt explicitly instructs the model to answer only from retrieved context and to refuse when information isn't present:
     - "You are a helpful assistant answering questions using ONLY the provided context documents.
     Rules:
          - Answer strictly using the information in the CONTEXT section below.
          - Do not use any outside knowledge, even if you know the answer.
          - If the context does not contain enough information to answer the question, respond exactly with: 'I don't have enough information on that.'
          - Do not speculate or fill gaps with general knowledge."

This is paired with a low temperature setting (0.1) to reduce the model's tendency to generate creative or speculative completions beyond what the context supports.


**How source attribution is surfaced in the response:**
     - Source attribution is not left to the LLM to generate or remember, it's handled programmatically. After retrieval, I collect the `source` metadata field from every retrieved chunk (deduplicated with `set()`), independent of what the model says in its answer text. This list is returned alongside the generated answer and displayed separately in the interface's "Retrieved from" field. This guarantees accurate source attribution even if the LLM's response text doesn't explicitly cite a source, and prevents the model from inventing or misremembering which document an answer came from.

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query:
     - Based on student reviews and forum advice, which specific business or finance professors are known to be strong mentors and write good recommendation letters, even if their classes are considered difficult?

Response:
     - Based on the student reviews, Dr. Denise Streeter in the Howard University Finance department is noted as a strong mentor who provides many opportunities for internships and supports students—even though her courses can be challenging.

Source attribution:
blackenterprise_howard_finance_careers.txt, 
ratemyprofessors_howard_business_finance.txt, thedig_mecca_wall_street_hps_center.txt

---

**Grounded response 2**

Query: 
     - What specific resources, training, or corporate pipelines does the HPS Center for Financial Excellence provide to help Howard students break into Wall Street?

Response:
     - The HPS Center for Financial Excellence (HPS-CFE) equips Howard students for Wall Street through a combination of mentorship, hands-on experience and a suite of structured programs that link directly to leading financial-services firms: Experiential learning programs (Investment Management Academy Scholars Program, Wealth Management Program, Wall Street on Campus), corporate guest speakers, workshops and bootcamps (interview prep, resume bootcamps, financial modeling, Bloomberg terminal training), a case-competition pipeline (Goldman Sachs' Market Madness competition), and strategic corporate partnerships.

Source attribution:
     - blackenterprise_howard_finance_careers.txt, 
     - husb_hps_center_students.txt, 
     - thedig_mecca_wall_street_hps_center.txt

---

**Out-of-scope query**

Query: 
     - What is the weather like in Antarctica?

System response (refusal):
     - I don't have enough information on that.
---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**
     - A single text box labeled "Your question," where the user types a natural-language question, plus an "Ask" button (the query can also be submitted by pressing Enter in the text box).

**Output format:**
     - Two separate read-only text boxes are displayed after submission:
          - **Answer** — the LLM-generated response, grounded in retrieved context
          - **Retrieved from** — a bulleted list of the source document filenames the answer draws from, generated programmatically from chunk metadata (not written by the LLM itself)


---

**Sample Interaction Transcript**

**User:** Based on student reviews and forum advice, which specific business or finance professors are known to be strong mentors and write good recommendation letters, even if their classes are considered difficult?

**System:** Based on the student reviews, Dr. Denise Streeter in the Howard University Finance department is noted as a strong mentor who provides many opportunities for internships and supports students—even though her courses can be challenging.

Retrieved from:
     -  blackenterprise_howard_finance_careers.txt
     -  ratemyprofessors_howard_business_finance.txt
     -  thedig_mecca_wall_street_hps_center.txt
<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->


---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->


| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|------------------|-------------------------------|--------------------|--------------------|
| 1 | Which finance professors are known to be strong mentors and write good recommendation letters? | | Identified Dr. Denise Streeter as a strong mentor who supports students and provides internship opportunities, despite challenging coursework | Relevant | Accurate |
| 2 | What is the exact timeline for finance/business recruiting per the HUSB guide, and what formal steps are needed? |  | "I don't have enough information on that." | Off-target (no chunk under 0.5 distance; correct source doc never appeared in top 5) | N/A - correctly refused (see Failure Case Analysis) |
| 3 | What resources/training/pipelines does the HPS Center for Financial Excellence provide for Wall Street recruiting? | | Detailed list of experiential programs, bootcamps, corporate partnerships, and the Goldman Sachs case-competition pipeline | Relevant | Accurate |
| 4 | What specific divisions of corporate/investment banking recruit at Howard per the Wells Fargo info session, and how can students leverage it? | | "I don't have enough information on that." | Relevant (top chunk at 0.207, correct source) | N/A - correctly refused (see Failure Case Analysis) |
| 5 | What do Reddit student anecdotes identify as Howard's unique advantage vs. other DC-area schools like American University? | | Cited Howard's "SOB" business program reputation and targeted recruiter interest as the key edge over schools like American University | Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target
**Response accuracy:** Accurate / Partially accurate / Inaccurate
---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
     - "Based on the HBCU Connect article about the Wells Fargo info session, what specific divisions of corporate and investment banking recruit at Howard, and how can students leverage these specific interactive sessions for networking?"

**What the system returned:**
     - "I don't have enough information on that."
**Root cause (tied to a specific pipeline stage):**
     - Retrieval succeeded — the correct chunk (distance: 0.207, the strongest match across all 5 evaluation questions) was retrieved from hbcuconnect_wells_fargo_howard_info_session.txt. However, inspecting the source document directly (both of its 2 chunks) shows the article only refers to a single umbrella group - "Corporate & Investment Banking (CIB)" — and never breaks this down into specific named sub-divisions. My evaluation question assumed a level of detail ("specific divisions," plural) that the source document does not actually contain.
**What you would change to fix it:**
     - This is not a retrieval or generation bug, it's a mismatch between the expected answer I wrote in planning.md and the actual depth of my source material. The system correctly declined to answer rather than inventing plausible-sounding division names, which is the grounding behavior the system prompt was designed to enforce. This highlights a limitation in my evaluation plan rather than my pipeline: future evaluation questions should be checked against actual source content before being finalized as "ground truth," not just written based on what I assumed the article would contain.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
     - Writing out a specific chunk size and overlap in planning.md before touching code gave me a concrete, testable target rather than a vague sense of "reasonable chunking." This mattered directly during debugging: when my initial retrieval test for a mentorship-related query returned only institutional program descriptions instead of actual professor reviews, I could point to a specific spec value (500 tokens) as the likely cause, rather than guessing broadly at what was wrong across the whole pipeline. Having a stated number to revisit and justify changing made the fix (200 tokens / 30 overlap) a deliberate, documented decision instead of trial-and-error tuning.

**One way your implementation diverged from the spec, and why:**
     - My planning.md's Retrieval Approach section assumed ChromaDB as the vector store, per the assignment's recommended stack. During implementation, ChromaDB failed to install on my machine, first blocked by a Windows Application Control policy preventing a required DLL from loading, then failing again when I tried an older version because it required compiling a C++ extension without the necessary build tools installed. Rather than fight a machine-level restriction I couldn't resolve, I implemented a lightweight numpy-based vector store using cosine similarity instead, which has no native dependencies and runs identically on any machine. Functionally, it fulfills the same requirement (semantic similarity search returning top-k chunks with metadata) but required writing my own similarity search logic rather than relying on ChromaDB's built-in query interface.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* My planning.md's Chunking Strategy section (500 tokens, 50 overlap) and pipeline diagram, and asked it to generate the document ingestion, cleaning, and chunking script (`ingest.py`).
- *What it produced:* A working script using tiktoken to chunk by token count at my specified 500/50 settings, with HTML-stripping and whitespace cleanup during preprocessing.
- *What I changed or overrode:* After running retrieval tests, I found that a query about professor mentorship returned only institutional program descriptions, not actual professor reviews. Inspecting my RateMyProfessors-style source document showed it contained 12 different professors' reviews, but at 500 tokens it was only producing 4 chunks, meaning 3+ unrelated professors were being merged into single chunks, diluting the embedding. I directed a change from 500/50 to 200/30 tokens, reran ingestion, and confirmed the same document now split into 9 chunks with individual professors distinguishable, and updated planning.md to reflect the new values and the reasoning.

**Instance 2**

- *What I gave the AI:* My retrieval and generation code (`retrieve.py`, `query.py`) and the exact terminal error output when `python retrieve.py` failed with a ChromaDB import error caused by a Windows Application Control policy blocking a required DLL.
- *What it produced:* First, a suggestion to downgrade ChromaDB to an older version without the problematic dependency. When that also failed (requiring C++ build tools I didn't have installed), it produced an alternative implementation: a numpy-based vector store using cosine similarity, with the same function signature (`retrieve(query, k)`)so the rest of my pipeline didn't need to change.
- *What I changed or overrode:* I accepted the numpy-based rewrite rather than continuing to troubleshoot ChromaDB installation on a machine I don't have full administrative control over, and documented this substitution and its cause (system-level restriction, not a code or design flaw) in planning.md's Retrieval Approach section, since it diverged from the assignment's recommended stack.

## DEMO Video Link
Watch the demo video here --> [https://youtu.be/Xrylu1VE9Ko]
 