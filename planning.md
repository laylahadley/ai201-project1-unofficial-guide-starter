# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Domain:
     - Internship and Recruiting Knowledge for Howard University Finance and Business Students

Why is this domain useful:
     - For finance and business students at Howard University, securing highly coveted internships (particularly in investment banking, corporate finance, and consulting) requires more than just a high GPA. The recruiting timeline for Wall Street and top business firms is notoriously accelerated and highly competitive. This domain provides the tactical "playbook" for success by synthesizing both formal institutional resources and informal student networks.
          - targeted interview prep
          - relevant extracurriculars
          - mentorship
          - networking methods

Why is this knowledge hard to find through official channels?
     - While Howard University provides excellent formal resources (like the HUSB Recruitment Guide and the HPS Center websites), the most critical recruiting intelligence exists in a "whisper network." This information is rarely found in official university brochures because:
          - nuance and unwritten rules: Official channels will tell a student to "get involved in student organizations." They will not explicitly tell a student which specific organizations have the most aggressive interview prep regimens, or which club's alumni base routinely fast-tracks resumes past the initial HR screening.
          - Real-Time Student Experiences: News (like The Dig) highlights successful outcomes and high-level corporate partnerships. However, the granular, day-to-day reality of the recruiting grind, i.e. how to answer specific technical questions, how to handle rejection, or how Howard compares locally to schools like American University, is primarily shared through anonymous forums like Reddit and HBCU Connect.
          - Rapidly Changing Recruiting Landscapes: Firm preferences and recruiting timelines shift year to year. Informal channels update much faster than a university's official annual recruitment PDF, giving students a real-time pulse on when applications actually open and close.



---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
