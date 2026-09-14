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
     - 500 tokens (roughly 1,500 to 2,000 characters)

**Overlap:**
     - 50 tokens (roughly 150 to 200 characters)

**Reasoning:**
     - This corpus contains a highly diverse mix of document structures, requiring a balanced chunking approach:
          - For the short-form content (RateMyProfessors, Reddit threads): A 500-token chunk is large enough to encompass an entire individual Reddit comment or multiple consecutive RateMyProfessors reviews. This prevents a single sentence of a student's anecdote from being stripped of its surrounding context (e.g., separating the professor's name from the critique of their grading style).
          - For the long-form content (News articles, University websites, PDF Guide): 500 tokens is ideal for isolating specific themes, like a single program description from the HPS Center website, or one particular recruiting timeline phase from the HUSB Recruitment Guide, without pulling in irrelevant sections.
          - The 50-token overlap acts as a safety net for the longer texts. It ensures that when a continuous thought, timeline step, or interview anecdote gets split between two chunks, the retrieval system doesn't lose the connecting sentence that ties the context together.
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
     - BAAI/bge-m3 (via HuggingFace/sentence-transformers)

**Top-k:**
     - (This retrieves approximately 2,500 tokens of context, which provides a diverse mix of sources without overwhelming the LLM's context window or diluting the answer with irrelevant chunks).

**Production tradeoff reflection:**
     - If cost and compute were not constraints for a real-world deployment, here is how I would weigh the architectural tradeoffs:
          - Accuracy on domain-specific text: The corpus contains a mix of highly formal corporate/academic text (recruitment guides) and highly informal, culturally specific slang (Reddit threads discussing "The Mecca," "HUSB," and Wall Street "superdays")
          - Context length: my current strategy uses 500-token chunks. However, if I wanted to preserve the entire narrative of a multi-page PDF recruitment guide or a deeply nested, multi-comment Reddit thread in a single vector, I would weigh upgrading to a model with a massive context window (such as Qwen3-Embedding-8B, which supports up to 32,000 tokens).
          - Latency: For a student-facing chatbot, real-time response is critical. Using a massive model with 3,072 dimensions might slightly increase retrieval accuracy (MTEB score) but would increase vector database storage, compute costs, and retrieval latency.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 |Based on student reviews and forum advice, which specific business or finance professors are known to be strong mentors and write good recommendation letters, even if their classes are considered difficult?
 |Based on RateMyProfessors and Reddit ("incoming students" thread), students frequently advise looking past strict grading rubrics to find mentors. While specific professors are often flagged as "tough graders" or having heavy workloads, the "whisper network" emphasizes that these exact professors, particularly those with long-standing industry connections in the finance department, are the ones who write the most influential, personalized letters of recommendation and directly refer students to Wall Street alumni. |
| 2 |According to the 2022-2023 HUSB Recruitment Guide, what is the exact timeline for finance and business recruiting, and what are the formal steps I need to take to prepare my application?  
|According to the official HUSB (Howard University School of Business) Recruitment Guide, the primary recruiting timeline centers around the Fall and Spring career fairs, with major Wall Street and corporate finance firms often fast-tracking applications early in the Fall semester. The formal steps require students to engage directly with the Office of Career Services, polish their resumes for official "resume drops," attend mandatory corporate information sessions, and submit applications strictly adhering to firm deadlines. |
| 3 |What specific resources, training, or corporate pipelines does the HPS Center for Financial Excellence provide to help Howard students break into Wall Street? |The HPS Center for Financial Excellence provides a direct pipeline to Wall Street by offering specialized academic concentrations, including Investment Banking, Capital Markets & Trading, and Private Equity. According to Howard's website and The Dig, the Center features the "Wall Street on Campus" initiative, which brings practicing professionals directly to students for interactive experiences. It is specifically mandated to increase diversity in elite financial services by bridging academic theory with real-world executive mentorship. |
| 4 |Based on the HBCU Connect article about the Wells Fargo info session, what specific divisions of corporate and investment banking recruit at Howard, and how can students leverage these specific interactive sessions for networking? |The HBCU Connect article specifically highlights that the Corporate & Investment Banking (CIB) division of Wells Fargo recruits directly at Howard. Students are advised to leverage these interactive sessions by networking directly with visiting professionals, program managers, and recruiters to secure "exclusive tips" on the hiring process. Furthermore, attendees who register and participate often gain access to secondary, invite-only networking opportunities like private "coffee chats" to stand out from the broader applicant pool.|
| 5 |When comparing Howard to other DC-area schools like American University, what do student anecdotes on Reddit identify as Howard's unique advantage for securing top finance internships? |On the Reddit r/HowardUniversity thread, student anecdotes strongly assert that Howard's School of Business (SOB) provides vastly superior recruiting opportunities compared to American University, George Washington (GW), or George Mason. The unique advantage is the targeted corporate pipeline: students note that top financial firms explicitly seek out Howard to recruit Black talent. Students claim that combining the cultural environment of the HBCU experience with this highly targeted, top-tier corporate recruiting makes the Howard experience, and subsequent internship placements, significantly better than attending a PWI in the same city. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Semantic mismatch between formal and informal sources
     - The risk - The retriever may fail to connect a user's informal query to official resources, or vice versa, causing critical information to be ignored.
     - the reasoning - The corpus contains a stark contrast in vocabulary. Official documents use formal corporate terminology ("Information Session," "Corporate & Investment Banking," "HUSB"), while Reddit and RateMyProfessors rely on student slang and industry shorthand ("superday," "sweaty," "target school," "GPA killer"). A standard embedding model might fail to recognize that a student asking about "IB pipelines" is semantically looking for the "HPS Center for Financial Excellence," leading to poor retrieval precision.

2. Conflicting claims and source authority confusion
     - the risk - The LLM may generate contradictory or misleading advice by blending official university policy with subjective student grievances.
     - the reasoning - RAG systems struggle when presented with conflicting evidence without explicit metadata weighting. For example, the HUSB Recruitment Guide might promote a specific mandatory course as an "essential networking step," while a RateMyProfessors chunk might strongly advise students to avoid that exact professor to protect their GPA. If the system does not explicitly attribute these chunks to their distinct sources (official policy vs. subjective peer review), it may confidently output contradictory instructions to the user.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

flowchart 


    %% Define styles for clarity
    classDef ingest fill:#f9f871,stroke:#333,stroke-width:1px,color:#333
    classDef chunk fill:#ffc75f,stroke:#333,stroke-width:1px,color:#333
    classDef embed fill:#ff9671,stroke:#333,stroke-width:1px,color:#333
    classDef store fill:#d4a5a5,stroke:#333,stroke-width:1px,color:#333
    classDef retrieve fill:#ff6f91,stroke:#333,stroke-width:1px,color:#333
    classDef generate fill:#d65db1,stroke:#333,stroke-width:1px,color:#fff
    classDef input fill:#845ec2,stroke:#333,stroke-width:1px,color:#fff

    %% Nodes and Pipeline Flow
    Q([User Query]) ::: input
    
    subgraph Data Pipeline
        direction TB
        A[1. Document Ingestion<br>BeautifulSoup & pdfplumber] ::: ingest
        B[2. Chunking<br>LangChain Recursive Splitter<br>Size: 500 | Overlap: 50] ::: chunk
        C[3. Embedding<br>sentence-transformers<br>bge-m3] ::: embed
        D[(Vector Store<br>ChromaDB)] ::: store
        
        A --> B --> C --> D
    end

    subgraph Query Execution
        direction TB
        R[4. Retrieval<br>ChromaDB Retriever<br>Top-k = 5] ::: retrieve
        G[5. Generation<br>LLM <br>Gemini / Claude] ::: generate
    end

    %% Connect the flows
    Q --> R
    D -. Fetches Chunks .-> R
    R --> G
    G --> Ans([Final Answer]) ::: input
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
