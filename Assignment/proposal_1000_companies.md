# Proposal — Building 1000 ICP-Qualified Companies in One Month

## Goal
Build a verified list of 1000 Indian specialty manufacturing companies that match DeepThought’s Federer ICP: promoter-driven, ₹50Cr–₹500Cr revenue, technical/differentiated products, technical decision-maker, and visible growth signals.

## Sourcing methods beyond Google

### 1. DSIR-recognized in-house R&D units
Why it works: DSIR recognition is a direct signal of R&D investment and technical seriousness.
Limitation: It may miss young companies that have not applied for DSIR recognition.

### 2. Trade expo exhibitor lists
Examples: ChemExpo India, India Chem, CPHI India, analytica Anacon, Medical Fair India, Agri Intex.
Why it works: Specialty manufacturers show up at focused expos because they sell technical products.
Limitation: Exhibitor lists include traders, distributors and overseas principals, so filtering is needed.

### 3. Regulatory and certification databases
Examples: CDSCO, USFDA, EU-GMP, ISO/AS9100, FSSAI, APEDA/export promotion councils.
Why it works: Certifications signal differentiated products, regulated manufacturing and export readiness.
Limitation: Databases may not expose revenue or ownership.

### 4. Export/import shipment intelligence
Examples: Volza, ImportGenius, EximPedia, Zauba import-export records.
Why it works: Exporting specialty products is a growth signal and helps separate manufacturers from local traders.
Limitation: Subscription cost and product-code ambiguity.

### 5. MCA/Tofler/Tracxn/Probe
Why it works: Revenue band, director names, age of company, charges, and filings can verify ICP fit.
Limitation: Financials may lag by one year and require paid access for speed.

### 6. LinkedIn/Naukri hiring signals
Why it works: Hiring 5+ roles is one of the assignment’s explicit growth signals.
Limitation: Smaller companies may hire informally, so absence of listings is not proof of stagnation.

## 1000-company one-month funnel

### Target funnel
Raw universe: 4000 companies  
After hard filters: 2200  
After automated ICP scoring: 1300  
After human QA: 1000 final verified companies

## Automation plan
1. Scrape or export company names, websites, city, segment and source URL from DSIR, expos, directories and databases.
2. Normalize names and remove duplicates using fuzzy matching.
3. Enrich each company with website text, LinkedIn page, MCA/financial source, decision-maker names, revenue estimate, and hiring signals.
4. Apply rule-based hard filters:
   - no website,
   - trader/distributor,
   - revenue above ₹500Cr,
   - acquired/PE-controlled,
   - no India manufacturing,
   - generic pharma/bulk commodity.
5. Use an LLM scoring prompt for the six criteria, but force source-backed evidence for every score.
6. Human-review all A/B rows with low confidence and all borderline C rows.

## Quality control
- Each company must have at least two independent sources.
- Every criterion score must include evidence, not just an assertion.
- Auto-disqualified rows are retained in a fail log to prevent rework.
- 10% of accepted rows are rechecked by a second reviewer or second LLM prompt.
- Revenue and ownership get highest priority because they are the most common hidden disqualifiers.

## Weekly execution plan

### Week 1 — Universe building
Build 4000 raw leads from DSIR, expo lists, trade associations, paid databases, and export directories.

### Week 2 — Enrichment and hard filtering
Collect websites, cities, product descriptions, revenue estimates, founder/MD names, ownership status and manufacturing evidence. Remove obvious non-fits.

### Week 3 — Scoring and evidence writing
Run automated Federer scoring, create personalization hooks, and classify A/B/C/D. Human-check all high-potential companies.

### Week 4 — Final QA and packaging
Resolve missing fields, validate revenue/ownership, remove false positives, and deliver the final CSV, fail list, methodology, and sourcing notes.

## Hand-drawn diagram to send in Internshala chat
Draw this on paper:

Raw sources → Deduplication → Hard filters → Automated enrichment → Federer scoring → Human QA → Final 1000 list

Under each stage, write the tools:
DSIR / expos / MCA / LinkedIn / Naukri / Volza / company websites / AI scoring / manual review.

Add three QA checkpoints:
1. Revenue below ₹500Cr
2. Promoter-driven / not acquired
3. Manufactures technical product in India
