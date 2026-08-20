#!/usr/bin/env python3
"""
Generate one full-text reader page per FULGME Journal article.

Every word of body text, every figure caption, every reference, and every
number below is transcribed from the article PDFs. Nothing is inferred,
summarized, or invented.

To build a new issue: copy this file, replace ISSUE and ARTICLES, run it.

Body block types:
  ("h2",  text)                     section heading
  ("h3",  text)                     subsection heading
  ("p",   html)                     paragraph
  ("ul",  [items])                  bullet list
  ("ol",  [items])                  numbered list
  ("olA", [(bold_lead, rest), ...]) numbered list with bold lead-ins
  ("fig", {src, alt, caption, cls}) figure
  ("tbl", html)                     table block (already marked up)
"""
import html, json, pathlib

SITE = "https://journal.fulgme.org"

ISSUE = {
    "num": "3", "label": "Issue 3", "code": "2026:00/03",
    "running_head": "Issue 3",          # FULGME publishes issues, not volumes
    "published": "August 2026", "pub_iso": "2026-08",
    "issue": "3", "issn": "3065-582X",
    "journal_doi": "10.70785/IHSN6820", "issue_doi": "10.70785/JJXN8215",
    "issue_pdf": "FULGME-Journal-Issue-3-August-2026.pdf",
    "path": "issue-3",
}

COI = "The author(s) declares no conflict of interest."

ARTICLES = [
# ----------------------------------------------------------------- A1
{
 "slug": "a1", "id": "A1", "type": "Brief Report", "special": None,
 "title": "Program Coordinator Well-Being Initiative: A Year in Review",
 "authors": [{"name": "Brant Weindorf", "aff": 1}],
 "affiliations": ["University of South Alabama, AL"],
 "cite_authors": "Weindorf B",
 "doi": "10.70785/EKFN3359",
 "pages": "1-5",
 "pdf": "FULGME_Vol_3_A1_August_2026.pdf",
 "abstract_structured": [
   ("Background", "Program coordinators are essential to the success of graduate medical education programs, yet their well-being is often overlooked."),
   ("Objective", "To evaluate whether a low-cost, coordinator-led wellness initiative improves workplace engagement, sense of community, and overall well-being among program coordinators over one year."),
   ("Methods", "In response to survey findings that identified concerns related to workplace resources, isolation, and overall well-being, a coordinator-led wellness initiative was implemented. Coordinators were surveyed in early 2024 and again in early 2025."),
   ("Results", "After one year, participants reported improvements in workplace engagement, sense of community, and overall well-being."),
   ("Conclusions", "These findings suggest that low-cost, coordinator-focused wellness initiatives can positively impact job satisfaction and professional connectedness."),
 ],
 "abstract_plain": "Program coordinators are essential to the success of graduate medical education programs, yet their well-being is often overlooked. This brief report evaluates whether a low-cost, coordinator-led wellness initiative improves workplace engagement, sense of community, and overall well-being among program coordinators over one year.",
 "body": [
  ("h2", "Background"),
  ("p", "Wellness as an ACGME requirement is a pillar of graduate medical education training. This aspect can often be unincorporated into the work lives of those who make these programs function, the program coordinator. At our institution, there was a palpable sense of isolation, burnout, and poor work-life balance among coordinators that was leading to high turnover, low job satisfaction, and poor employee performance."),
  ("h2", "Objectives"),
  ("p", "This report shows a one year evaluation of a multispecialty sample of graduate medical education program coordinators regarding their perceptions of isolation, burnout, and work-life balance. It seeks to show the need for program coordinator specific wellness initiatives and the current and projected success of this wellness initiative within the constraints of little to no budget."),
  ("h2", "Methods"),
  ("p", "In early 2024, the authors surveyed program coordinators within residency and fellowship programs concerning their current job relationship. These program coordinators answered questions on various aspects of their work day, job satisfaction, and view of graduate medical education. The index questions for this report asked, &ldquo;Do you look forward to coming to work most days?&rdquo; (Yes or No), &ldquo;Have you ever felt or do you feel isolated at work?&rdquo; (Yes or No), and &ldquo;How satisfied or dissatisfied are you in your current role?&rdquo; (1 for Very dissatisfied to 5 for Very satisfied). Another follow up survey was conducted in early 2025 with similar questions, a few demographics removed, and new questions of the effectiveness of the wellness initiative. Analysis consisted of basic comparative and descriptive statistics."),
  ("h2", "Results, Outcomes, and Improvements"),
  ("p", "The initial survey had troubling statistics of poor well-being that confirmed initial observations. 56.2% of coordinators felt they did not have enough resources to be successful in their role. 31.3% said they felt burnt out. One comment specified a need for &ldquo;more communication/social [aspects] with other coordinators.&rdquo;"),
  ("fig", {"src": "figures/figure-1.jpg",
           "alt": "Bar chart titled Resource Adequacy Among Program Coordinators, March 2024. Insufficient resources 56.2 percent, adequate resources 43.8 percent, shown as percent of respondents.",
           "caption": "<b>Figure 1.</b> Resource Adequacy Among Program Coordinators (March 2024). Percentage of program coordinators who reported that they did not have enough resources to be successful in their role."}),
  ("p", "In combination with these results and national data, a year of program coordinator wellness events were planned through a committee founded by the two authors called Program Coordinators Advocating for Wellness (PCAW). Events would occur every other month and during less stressful months in the academic year. Six events took place from March 2024 to November 2024. These initiatives targeted aspects of wellness, had no initial cost associated with them, and utilized existing opportunities within the institution. Two were after-hours dinner events, two were during work hours potluck and lunch gatherings, one was a private yoga session, and one was a group field trip to a local farmer&rsquo;s market on campus. Food-based events proved to be the most engaged-with type of event with yoga being a close second. Planning for future events will target each aspect of the wellness wheel per event."),
  ("p", "The follow-up survey had significant improvements in data. Looking forward to work increased from 43.8% to 75%. Feeling isolated at work decreased from 50% to 37.5%. Overall job satisfaction increased by 18%. Overall well-being increased from 50% to 87.5% following the implementation of wellness initiatives. 100% of our responders said PCAW improved their sense of community with other coordinators, sense of well-being, and work-life balance in GME. One comment said that &ldquo;[PCAW] really creates a sense of &lsquo;belonging&rsquo; for me.&rdquo; There were some noted variables in data due to job changes."),
  ("fig", {"src": "figures/figure-2.jpg",
           "alt": "Grouped horizontal bar chart titled Impact of the PCAW Wellness Initiative, comparing March 2024 and March 2025. Overall well-being 50.0 percent to 87.5 percent. Look forward to work 43.8 percent to 75.0 percent. Feel isolated at work 50.0 percent to 37.5 percent.",
           "caption": "<b>Figure 2.</b> Impact of the PCAW Wellness Initiative. Comparison of March 2024 and March 2025 survey responses. Lower percentage for isolation indicates improvement."}),
  ("h2", "Conclusion"),
  ("p", "Wellness needs to be incorporated into graduate medical education offices with program coordinators as the focus. Having activities and events for program coordinators is a way to make sure job retention increases and that the support residents need is consistent. Initiatives need to be cost-effective to ensure replication in other institutions. Further evaluations of this wellness initiative will come at year milestones to showcase longevity and practicality of wellness in the workplace."),
 ],
},
# ----------------------------------------------------------------- A2
{
 "slug": "a2", "id": "A2", "type": "Perspective", "special": None,
 "title": "Centering the Role of the GME Director in Institutional Success",
 "authors": [{"name": "Lisa Payne", "aff": 1}, {"name": "Donna Guidroz", "aff": 2},
             {"name": "Melody Alijani, MS", "aff": 3}],
 "affiliations": ["UCLA", "Ochsner Health",
                  "University of Nevada, Reno School of Medicine"],
 "cite_authors": "Payne L, Guidroz D, Alijani M",
 "correction": {
   "date": "18 August 2026",
   "text": ("Melody Alijani, MS, University of Nevada, Reno School of Medicine, was added as the third "
            "author of this article. The author list, the affiliations, and the recommended citation on "
            "this page have been updated. The article PDF and the full issue PDF have been reissued with the "
            "corrected author list. No other part of the article has changed."),
 },
 "doi": "10.70785/LLJT5147",
 "pages": "2-5",
 "pdf": "FULGME_Vol_3_A2_August_2026.pdf",
 "abstract_structured": None,
 "abstract_plain": "Graduate Medical Education (GME) Directors are essential to the operational and regulatory success of residency and fellowship programs, yet their contributions often remain underrecognized. Drawing on findings from the 2025 GME Director Survey, this article highlights the evolving role of GME Directors, the challenges they face, and the importance of strengthening their authority, visibility, and leadership development. It also emphasizes the value of physician-administrator dyad leadership and calls for greater institutional investment in these professionals to ensure the long-term success and sustainability of graduate medical education.",
 "body": [
  ("h2", "Introduction"),
  ("p", "Behind every compliant, learner-centered, and mission-driven graduate medical education (GME) program is a GME Director, a professional whose formal job description captures only a fraction of their contributions. While Program Directors, faculty, and institutional leaders are the clinical and academic face of residency and fellowship programs, GME Directors provide the operational and regulatory integrity that allows those programs to function. They are the quiet foundation, the throughline across systems, programs, and people."),
  ("p", "A national survey conducted in 2025, <i>The GME Director Survey: Summary Report</i>, gathered insights from 101 GME Directors and senior institutional leaders across a wide range of institution types and sizes, from academic medical centers to community hospitals. It revealed an experienced, highly educated workforce navigating increasingly complex responsibilities. These professionals are essential to program stability and compliance, yet their authority often does not match the scope of their work. This article synthesizes those findings to highlight the indispensable role of GME Directors and calls for intentional investment in their authority, visibility, and development, especially as dyad partners alongside physician leaders."),
  ("h2", "A Highly Qualified Yet Under-Empowered Workforce"),
  ("p", "The survey found that 72% of GME Directors hold a graduate or professional degree, and 57% have worked in GME for more than a decade. Many have advanced internally, with 30% previously serving as residency or fellowship coordinators. This path reflects deep institutional memory and a strong commitment to academic medicine. Despite their qualifications, only 52% reported having sufficient authority to fulfill their role. Another 36% answered &ldquo;somewhat,&rdquo; while 12% said they lacked meaningful authority entirely. Barriers to effectiveness include:"),
  ("ul", ["Limited decision-making power (57%)",
          "Insufficient resources (52%)",
          "Undefined roles and responsibilities (50%)",
          "Limited influence as non-physicians (43%)"]),
  ("p", "These limitations are systemic. They hinder GME leaders from operating at their full potential and, if left unaddressed, they risk institutional compliance and trainee support."),
  ("h2", "Responsibility Without Recognition"),
  ("p", "The survey showed a clear disconnect between the responsibilities GME Directors carry and the ways their success is measured. Nearly all respondents are accountable for:"),
  ("ul", ["ACGME compliance (98%)",
          "Budget and financial oversight (86%)",
          "Institutional goal execution (82%)",
          "Program growth and innovation (74%)"]),
  ("p", "Yet the most frequently cited weekly challenges included:"),
  ("ul", ["Managing HR and personnel issues (67%)",
          "Space and facility constraints (54%)",
          "Day-to-day accreditation logistics (52%)",
          "Budget management and reconciliation (48%)"]),
  ("p", "A full 75% of respondents spend most of their time on operational logistics. These vital functions, including onboarding, documentation, faculty development, and compliance tracking, are often unrecognized in formal evaluations. This disconnect contributes not only to role ambiguity but also to burnout."),
  ("p", "Over 90% of GME Directors reported at least occasional burnout. A quarter (25%) cited frequent symptoms, and 7% reported constant burnout. These levels rival those of clinical providers, yet GME Directors rarely receive the same wellness supports, professional safeguards, or institutional prioritization."),
  ("h2", "The Role in Action: Beyond the Job Description"),
  ("p", "The survey also uncovered consistent themes in how GME Directors are stretched beyond their formal role. In addition to managing accreditation and budgets, many serve as:"),
  ("ul", ["Supervisors of large teams of program coordinators",
          "Interpreters of evolving ACGME standards",
          "Collaborators with HR, Legal, and Risk Management",
          "Institutional memory during leadership turnover",
          "First responders to crises such as natural disasters, unprecedented events, or systems failures"]),
  ("p", "These duties are critical to the functioning and compliance of GME programs. Yet they are rarely codified, measured, or resourced accordingly."),
  ("p", "GME Directors are often the first call when a resident has a concern, when faculty need support navigating a process, or when institutional leadership needs assurance that accreditation tasks are on track. Their work intersects directly with the experiences of residents and fellows, faculty, and physician leaders."),
  ("h2", "Dyad Leadership in Practice"),
  ("p", "The most effective institutions recognize that strong graduate medical education requires shared leadership. The dyad model pairs a physician leader, such as a Designated Institutional Official or Program Director, with an experienced GME administrator. This structure ensures that operational, academic, and clinical needs are jointly considered."),
  ("p", "This model works best when both members of the dyad are empowered, visible, and mutually respected. Physician leaders bring essential clinical insight and academic oversight. Administrative leaders provide operational continuity, regulatory expertise, and cross-departmental coordination. Together, they create a more resilient and responsive GME enterprise."),
  ("p", "But for this model to thrive, administrative GME leaders must be recognized as partners rather than support staff. This includes having a seat at strategic tables, participating in policy and curricular decisions, and being evaluated based on the full scope of their contributions."),
  ("h2", "Building the Infrastructure GME Needs"),
  ("p", "The findings of the 2025 survey point to five key institutional actions to better support GME Directors and strengthen the foundation of graduate medical education:"),
  ("olA", [
    ("Clarify and Standardize the Role.", "Job titles, core functions, and reporting lines should be aligned across institutions. A national consensus on role expectations can enhance recruitment, retention, and succession planning."),
    ("Include GME Directors in Strategic Decision-Making.", "Administrative GME leaders should participate in discussions about workforce planning, institutional growth, and policy implementation. Their foresight often prevents downstream accreditation or resource challenges."),
    ("Align Performance Metrics with Reality.", "Evaluation frameworks must reflect operational and leadership tasks, not compliance alone. Recognition for onboarding, coordinator supervision, and system-level risk management should be standard."),
    ("Invest in Leadership Development.", "Structured pipelines, including mentorship, TAGME certification, and leadership academies, are essential. Institutions should encourage professional growth and provide advancement opportunities within the GME structure."),
    ("Advance Dyad Partnerships Institutionally.", "Institutional support for physician-administrator collaboration should include shared goals, transparent communication, and co-led initiatives that advance the mission of GME."),
  ]),
  ("h2", "A Call for Further Research"),
  ("p", "The GME Director Survey represents a first-of-its-kind effort to formally document the scope, challenges, and insights of GME administrative leadership. However, more data are needed to fully understand:"),
  ("ul", ["The long-term impact of administrative leadership on program success",
          "The role of GME Directors in faculty and coordinator development",
          "Burnout and retention patterns among GME administrators",
          "Best practices in dyad leadership for medical education"]),
  ("p", "Ongoing research in these areas can guide national policy, accreditation standards, and institutional investment."),
  ("h2", "Conclusion: A Foundation Worth Strengthening"),
  ("p", "The success of GME programs depends on infrastructure as well as curricula and clinical exposure. GME Directors are the framework that supports accreditation, resident success, operational continuity, and compliance. Their work touches every part of the academic medical enterprise."),
  ("p", "By recognizing, resourcing, and recalibrating their role within the system, institutions can retain high-performing leaders and strengthen the quality and sustainability of GME itself."),
  ("p", "Let us make the invisible work visible."),
 ],
},
# ----------------------------------------------------------------- A3
{
 "slug": "a3", "id": "A3", "type": "Perspective", "special": None,
 "title": "Graduate Medical Education and the United States Military: Structure, Integration, and Comparative Perspectives",
 "authors": [{"name": "Theraesa Jones-Cleveland, BSHM, C-TAGME", "aff": 1}],
 "affiliations": ["Colorado Technical University", "Cleveland Clinic Foundation"],
 "cite_authors": "Jones-Cleveland T",
 "doi": "10.70785/XZGA3877",
 "pages": "3-5",
 "pdf": "FULGME_Vol_3_A3_August_2026.pdf",
 "abstract_structured": None,
 "abstract_plain": "This paper analyzes the relationship between Graduate Medical Education (GME) and the United States military. Drawing on quantitative data, comparative analysis, and firsthand experiences, it examines the structure of military GME programs, their integration within military healthcare, and the unique expectations placed on military trainees. Perspectives from physicians who have completed both military and civilian residencies, along with a representative case study, illustrate the challenges and advantages of each training pathway. The findings offer practical recommendations for medical students, educators, and policymakers to inform decision-making, curriculum development, and future discussions surrounding military and civilian medical education.",
 "body": [
  ("h2", "Introduction"),
  ("p", "Graduate Medical Education (GME) is the critical phase of medical training that follows medical school and leads to board certification. In the United States, GME is delivered through residency and fellowship programs accredited by the Accreditation Council for Graduate Medical Education (ACGME). The U.S. military, which comprises the Army, Navy, and Air Force, maintains its own GME infrastructure to train physicians for service in military healthcare systems. Understanding the interplay between GME and the military is vital for prospective military physicians, educators, and policymakers seeking to optimize medical training and readiness."),
  ("h2", "Military GME Programs: Structure, Quantitative Data, and Pathways"),
  ("p", "The Department of Defense (DoD) oversees military GME programs across the Army, Navy, and Air Force. Each branch operates in medical centers and hospitals hosting ACGME-accredited residency and fellowship programs. In 2024, the military trained approximately 2,600 physicians annually across its GME programs, with the Army accounting for roughly 1,000 trainees, the Navy for 800, and the Air Force for 800. These programs span a variety of specialties, including internal medicine, surgery, psychiatry, and emergency medicine, and are designed to meet both civilian standards and military needs such as operational readiness and deployment preparation. Admission is typically reserved for individuals committed to military service, often through the Health Professions Scholarship Program (HPSP) or the Uniformed Services University of the Health Sciences (USUHS) pathway. Trainees are commissioned officers, receiving benefits and obligations associated with military service, including deployment readiness and leadership training."),
  ("h2", "Comparison: Military vs Civilian GME Programs"),
  ("p", "Both military and civilian GME programs adhere to ACGME standards, but notable differences exist. Military programs integrate military-specific training such as leadership development, operational medicine, and preparation for deployment, while civilian programs often focus on academic pursuits and research. Military hospitals prioritize care for active-duty personnel, their families, and veterans, resulting in a patient population distinct from civilian institutions."),
  ("p", "Civilian programs are typically larger, with more diverse patient volumes and broader subspecialty training opportunities. For example, the average civilian residency program in internal medicine may train 30 to 50 residents annually, whereas military programs in the same specialty may train 10 to 20 residents per site. Research resources and subspecialty options are often more extensive in civilian centers, but military GME offers unique experiences, such as battlefield medicine and humanitarian missions."),
  ("fig", {"src": "figures/figure-1.jpg",
           "alt": "Bar chart titled Annual Military GME Trainees by Military Branch, Department of Defense 2024. Army 1,000 trainees, Navy 800 trainees, Air Force 800 trainees.",
           "caption": "<b>Figure 1.</b> Comparison of Military and Civilian Graduate Medical Education (GME). Annual Military GME Trainees by Military Branch (DoD, 2024)."}),
  ("tbl", """<table class="data">
        <caption>Table 1. Comparison of Military and Civilian Graduate Medical Education Programs</caption>
        <thead><tr><th scope="col">Feature</th><th scope="col">Military GME</th><th scope="col">Civilian GME</th></tr></thead>
        <tbody>
          <tr><th scope="row">Annual Trainee Volume</th><td>Approximately 2,600 (DoD, 2024)</td><td>Varies by institution; often larger</td></tr>
          <tr><th scope="row">Patient Population</th><td>Active-duty service members, families, and veterans</td><td>Diverse general population</td></tr>
          <tr><th scope="row">Service Obligations</th><td>Military service and deployment readiness</td><td>No military service required</td></tr>
          <tr><th scope="row">Leadership Training</th><td>Integrated and mandatory</td><td>Optional; less formalized</td></tr>
          <tr><th scope="row">Post-Residency Commitment</th><td>Service obligation (4&ndash;7 years)</td><td>No post-residency obligation</td></tr>
        </tbody>
      </table>
      <p class="tbl-note">Abbreviations: DoD = U.S. Department of Defense; GME = Graduate Medical Education. Source: U.S. Department of Defense, 2024.</p>"""),
  ("h2", "Military Trainees in Civilian GME: Anecdotal Experiences and Case Study"),
  ("p", "Not all military physicians complete their GME within military hospitals. Some are selected to train in civilian residency programs through &ldquo;deferred&rdquo; or &ldquo;sponsored&rdquo; positions, based on service needs and specialty availability. In 2024, about 15% of military GME trainees participated in civilian residencies. These individuals remain commissioned officers and are subject to military expectations, including participation in military activities and additional training."),
  ("p", "<b>Case Study:</b> Dr. Brandon Specht, an Air Force physician, began his medical career through HPSP, completing medical school in a civilian institution before entering a civilian Plastic Surgery residency. He reported challenges in balancing military obligations (such as attending quarterly training sessions and maintaining fitness standards) with the demands of civilian residency. However, he found that his exposure to diverse patient populations and advanced research opportunities enriched his surgical and clinical skills. Upon completion, Dr. Specht transitioned to a military hospital position as well as a position in a civilian clinic, where he adapted to military protocols and assumed leadership roles. He highlighted that the military&rsquo;s structured mentorship and operational training prepared him for potential deployment, as well as offering unique professional benefits."),
  ("h2", "Integration of GME in Military Structure: Impact and Outcomes"),
  ("p", "GME is a strategic component of the military healthcare system, ensuring a pipeline of board-certified physicians capable of meeting operational and clinical needs. Residency programs are closely aligned with the mission of military medical centers, which prioritize readiness, force health protection, and support for deployed operations. Military-trained physicians consistently demonstrate high adaptability, with 90% reporting readiness for deployment within six months of completing residency. The integration of GME within the military facilitates rapid responses to emerging medical challenges, such as trauma care innovations and infectious disease management."),
  ("h2", "Perspectives: Civilian vs Military Residency Experiences"),
  ("p", "Individuals who have completed both civilian and military residencies cite cultural and structural differences. Military residencies emphasize teamwork, chain of command, and deployment readiness, while civilian programs focus on academic pursuits and research. Military residents may face additional administrative duties and training scenarios, such as mass casualty drills and leadership courses. Civilian-trained military physicians appreciate the broader patient populations and research resources but require adaptation to military protocols upon returning to service. Flexibility and commitment to the values of both medicine and military service are essential for successful transitions."),
  ("h2", "Recommendations: For Medical Students and Educators"),
  ("h3", "For Medical Students Considering Military Service"),
  ("ul", ["Evaluate personal goals, willingness to serve, and readiness for military obligations.",
          "Research specialty availability and training environments in both military and civilian pathways.",
          "Seek mentorship from current or former military physicians to understand career trajectories and challenges.",
          "Consider the impact of service obligations on long-term career plans, including deployment and leadership opportunities."]),
  ("h3", "For Educators Designing Curricula"),
  ("ul", ["Integrate modules on operational medicine, leadership, and military ethics into civilian curricula for students interested in military careers.",
          "Facilitate collaborative training opportunities between civilian and military institutions to bridge gaps in experience and knowledge.",
          "Encourage research and case-based learning that addresses both civilian and military healthcare challenges.",
          "Support students in navigating dual identities and obligations through structured guidance and counseling."]),
  ("h2", "Conclusion"),
  ("p", "The relationship between GME and the military is multifaceted, reflecting the dual imperatives of medical excellence and operational readiness. Military GME programs are structured to produce physicians capable of serving in both clinical and operational contexts. Quantitative data and case studies show the unique opportunities and challenges faced by military trainees, particularly those navigating civilian residencies. Insights from this analysis inform decision-making for prospective physicians, educators, and policymakers by highlighting the importance of flexibility, mentorship, and curriculum integration."),
  ("p", "For policymakers, understanding the comparative features of military and civilian GME can guide resource allocation, specialty development, and recruitment strategies. For educators, designing curricula that bridge civilian and military training environments ensures that future physicians are prepared for diverse professional demands. Prospective medical students benefit from informed decision-making regarding military service, specialty selection, and career planning. Continued collaboration between civilian and military institutions will enhance the quality and readiness of the U.S. physician workforce, supporting both healthcare delivery and national security."),
 ],
},
# ----------------------------------------------------------------- A4
{
 "slug": "a4", "id": "A4", "type": "Brief Report", "special": None,
 "title": "Building a Collaborative Network for GME Coordinators in Puerto Rico: A Social Media-Based Approach",
 "authors": [{"name": "Cristina Morales, MBA, C-TAGME", "aff": 1}],
 "affiliations": ["Mayaguez Medical Center, Family Medicine Residency Program, Puerto Rico"],
 "cite_authors": "Morales C",
 "doi": "10.70785/ZMUQ2206",
 "pages": "4-5",
 "pdf": "FULGME_Vol_3_A4_August_2026.pdf",
 "abstract_structured": [
   ("Background", "Graduate Medical Education (GME) coordinators play an essential role in residency program administration, yet opportunities for collaboration and professional development can be limited, particularly in geographically isolated regions."),
   ("Objective", "To describe the development and early engagement of a social media-based network for GME coordinators and administrators in Puerto Rico."),
   ("Methods", "This brief report describes the development of the PR GME Coordinators &amp; Administrators Facebook group, a social media-based initiative designed to encourage networking, resource sharing, and peer support among GME professionals across Puerto Rico."),
   ("Results", "Early engagement demonstrates the feasibility of using an accessible digital platform to build a collaborative community of practice, promote professional development, and strengthen administrative consistency across institutions."),
   ("Conclusions", "This scalable, low-cost model offers a practical approach that may be adapted to support GME coordinators in other resource-limited or geographically dispersed settings."),
 ],
 "abstract_plain": "Graduate Medical Education (GME) coordinators play an essential role in residency program administration, yet opportunities for collaboration and professional development can be limited, particularly in geographically isolated regions. This brief report describes the development and early engagement of the PR GME Coordinators and Administrators Facebook group, a scalable, low-cost model for building a collaborative community of practice.",
 "body": [
  ("p", "Graduate Medical Education (GME) coordinators play a critical role in supporting residency programs; however, opportunities for structured collaboration and professional development among coordinators in Puerto Rico have been limited."),
  ("p", "To address the need for collaboration and professional development, a social media-based initiative was developed through the creation of the PR GME Coordinators &amp; Administrators Facebook group."),
  ("p", "This group was designed as an accessible and centralized platform for GME coordinators and administrators across Puerto Rico."),
  ("fig", {"src": "figures/prgme-logo.jpg", "cls": "logo",
           "alt": "Circular logo reading Puerto Rico GME, PRGME, Coordinators and Administrators.",
           "caption": "Logo of the PR GME Coordinators &amp; Administrators group."}),
  ("p", "The primary objectives of the group included:"),
  ("ul", ["Facilitating peer-to-peer discussions",
          "Sharing educational resources and best practices",
          "Promoting professional development opportunities and events",
          "Encouraging collaboration across institutions"]),
  ("p", "The platform was selected due to its accessibility, familiarity among users, and ability to support real-time communication and content sharing. This initiative was independently developed and implemented, demonstrating the potential for individual leadership to advance innovation in GME administration."),
  ("p", "Within the first three months, the group has grown to include over 25 members representing multiple institutions across Puerto Rico."),
  ("p", "Engagement within the group has included:"),
  ("ul", ["Active discussions among members",
          "Sharing of educational resources",
          "Promotion of professional development events"]),
  ("p", "This report describes an early-stage, social media-based approach to addressing a recognized gap in collaboration and professional development among GME coordinators in Puerto Rico. By using an accessible digital platform, this initiative shows how low-cost, scalable solutions can support meaningful professional engagement."),
  ("p", "This initiative extends beyond a communication tool by building a structured community of practice tailored to the specific needs of GME coordinators. By strengthening collaboration and administrative practices, it has the potential to indirectly enhance the quality and consistency of GME program operations."),
  ("p", "Despite its early stage, this initiative highlights the feasibility of implementing innovative solutions with minimal resources. While formal outcome measures are not yet available, future efforts will focus on incorporating structured evaluation methods, including participant feedback and engagement metrics."),
  ("p", "Future directions include the development of structured educational programming such as workshops, webinars, and local conferences in Puerto Rico aimed at further advancing the professional development of GME coordinators and administrators."),
  ("p", "Although this report reflects a single-region initiative, this model may be particularly valuable in geographically or resource-limited settings and can be adapted to similar contexts."),
 ],
},
# ----------------------------------------------------------------- A5
{
 "slug": "a5", "id": "A5", "type": "Perspective",
 "special": "New Board Member &middot; Special Section",
 "peer_reviewed": False,
 "title": "Perspectives: Look How Far We Have Come, a Lookback on the Evolution of the GME Coordinator Role",
 "authors": [{"name": "Crys S. Curkendoll-Draconi, PMP, AA", "aff": 1}],
 "affiliations": ["Cleveland Clinic South Pointe Hospital"],
 "cite_authors": "Curkendoll-Draconi CS",
 "doi": "10.70785/YCCD4272",
 "pages": "5-5",
 "pdf": "FULGME_Vol_3_A5_August_2026.pdf",
 "abstract_structured": None,
 "abstract_plain": "Graduate medical education (GME) has changed substantially over the past two decades, reshaping the responsibilities and professional identity of the GME Coordinator. This perspective reflects on the evolution of the role from primarily administrative support to a highly specialized profession essential to accreditation, regulatory compliance, educational operations, and trainee success. Through the lens of personal experience, the article traces key milestones in GME, including the implementation of the ACGME Core Competencies, Milestones, and the Next Accreditation System, while highlighting the grassroots advocacy efforts that led to formal recognition of the coordinator role within ACGME Common Program Requirements. Although significant progress has been made in professional development, recognition, and career advancement, continued advocacy, collaboration, and mentorship remain essential to ensuring the role continues to evolve alongside the changing landscape of graduate medical education.",
 "body": [
  ("h2", "Introduction"),
  ("p", "I never thought I would be saying this, but I have been in the graduate medical education (GME) world for a long time, since September 2008. I took my first GME role as part of a combined role that I hoped to use as a steppingstone to my next phase in my career. Today I can say that is exactly what happened, but never in the way I had imagined. I never knew this role existed until I was sucked into it, and it has certainly grasped onto me and never let go."),
  ("h2", "History of the GME Administrator"),
  ("h3", "Pre-Competencies"),
  ("p", "Although when I started my first GME Administrator role, it was not long after that the ACGME developed the core competencies, through what they called the &ldquo;Outcome Project&rdquo; (ACGME, n.d.).<sup><a href=\"#ref1\">1</a></sup> In 2001, these competencies were established and just like most new regulations took a few years to figure out how to implement them. Believe it or not, these did not always exist and before this the requirements were a lot easier to keep up with. This meant a strong coordinator, although it was nice to have one, it was not 100% necessary, especially in smaller programs and specialties. Many times, programs had a coordinator, but there was no requirement for it and very well-versed secretaries were most likely the top pick for these roles as they were close to 100% administrative through scheduling, communication, event planning, etc. Administrators stayed in their roles for long periods of time, sometimes even retirement."),
  ("h3", "Competencies"),
  ("p", "With the establishment of the competencies, it gave the programs at least a guideline of the basic skills that graduate medical education trainees should walk away with to practice medicine successfully. However, that meant more oversight for the program administrators. Therefore, it was a bit more challenging than it had been in past years to find the best qualified people for these roles. Although they could learn many skills, they had to be much more independent. The frustration was starting to build in these roles because they did not receive proper training or orientation to the role and flew by the seat of their pants. Around this time the discussion of Milestones was starting to take shape with the intention of this being implemented. Not a whole lot was said about what this would look like and the requirements that would come out of the coordinator&rsquo;s role to meet requirements. This created a lot of anxiety for the already overworked coordinator role. This is when a lot of coordinators who could, retired and others were looking for some sort of career trajectory, ladder and education."),
  ("h3", "Milestones and NAS"),
  ("p", "Then in 2013, the ACGME Milestones (ACGME, n.d.)<sup><a href=\"#ref2\">2</a></sup> along with the ACGME Next Accreditation System (Nasca T., 2012)<sup><a href=\"#ref3\">3</a></sup> started. Now I think if just one was introduced at a time, rather than both major changes, there may not have been such a large explosion of anxieties and needed learning to go along with it. The Next Accreditation System (NAS) was introduced as an entirely new process, in just about every way possible, to handle accreditation. Up to this point, reaccreditation was done based on the program and the Residency Review Committee&rsquo;s (RRC) decision, usually anywhere from two to five years and included a site visit and the dreaded Program Information Form (PIF). This new system was developed during a time of technological advances that a lot of these reaccreditation processes could be done via the WebADS (Accreditation Data System), which is now just ADS. Information about the program was now entered annually, and the implementation of a 10-year Self Study was established, and an annual accreditation cycle was formed. Site visits would still happen routinely, and as part of issues that may have popped up through this process. The Milestones were building on the Core Competencies to be more specific to help guide programs in their curriculum and evaluation of trainees. Although in the beginning they were meant to be specialty specific and were developed by the RRC members. In 2018, the ACGME started the Milestones 2.0 project (Edgar L, 2018),<sup><a href=\"#ref6\">6</a></sup> which was reviewing what had been done and improving upon it. The writing groups this time were not the RRC, but volunteers within the GME community including program directors, faculty, trainees, and possible coordinators. With all these changes it took many programs years to implement them properly. This also meant that coordinators had a much bigger role in the program and at the very least needed to understand and be part of the process of this assessment in ways they never had in the past."),
  ("p", "With all these changes and new responsibilities for coordinators, the frustration that was already building had come to a head. There were many people frustrated and feeling stuck and overwhelmed by the workload, and there still was no mention of the coordinator in the program requirements. This meant that programs and institutions may have recognized the need for the coordinator but may not have valued its importance. Out of this frustration, along with many colleagues, I created the Coordinator Description Task Force or CDTF (Schritz L, 2015),<sup><a href=\"#ref4\">4</a></sup> which was a grass roots effort completely ran by GME coordinators with no sponsorship. The main goal of this Task Force was to petition the ACGME to include language that outlined the need for a coordinator into the ACGME Common Program Requirements (ACGME, n.d.).<sup><a href=\"#ref5\">5</a></sup> The task force included representation from each core specialty in addition to anyone who wanted to take part. It included data collection through surveys, a collection of responsibilities and proposing new language. At the end we created a petition for the community to sign in support. During this time, the ACGME opened their suggestions for revisions to the requirements and developed the Coordinator Advisory Council. After much discussion, language was finally added to include the program coordinator but without the specifics beyond allotted FTEs based on program size for residencies and many fellowships."),
  ("h2", "Where are we now"),
  ("h3", "The Good"),
  ("p", "The good thing in all of this was it gave a voice to the frustration and was able to create many programs, training, support systems and tools to help better recognize and support those in these roles. It also gave the opportunity to really view the role as career and a profession, beyond being a job. With the community, and all the hard work they continually do to keep this profession moving forward including the implementation of more appropriate titles, more opportunities, and more networking and mentorship, we can continue to have positive outcomes for programs as a whole."),
  ("h3", "The Challenges"),
  ("p", "In my opinion, some of the challenges we still face include not letting all this work be forgotten. There will always be those that want to go back to the former ways, or to eliminate certain things they feel are unnecessary. We also want to continue to grow the role. We accomplished a lot of things, but that doesn&rsquo;t mean we are 100% of the way &ldquo;there&rdquo;. Continue to get involved in the community, and don&rsquo;t get stuck in the &ldquo;island&rdquo; syndrome where you are figuring this out by yourself. Get involved, and don&rsquo;t worry about if you are afraid that your voice won&rsquo;t matter, no matter what the subject. We are a very important and integral part of the progress in GME, even without medical degrees."),
 ],
 "references": [
   'Competency-Based Medical Education: A Brief History and Primer. (n.d.). <a href="https://www.acgme.org/globalassets/pdfs/competency-based-medical-education_a-brief-history-and-primer.pdf">https://www.acgme.org/globalassets/pdfs/competency-based-medical-education_a-brief-history-and-primer.pdf</a>',
   'Warm, E., Kelleher, M., Kinnear, B., Sall, D., Luciano, G., Holmboe, E., &amp; Rosenblum, M. (n.d.). Accreditation Council for Graduate Medical Education A GUIDEBOOK FOR IMPLEMENTING AND CHANGING ASSESSMENT IN THE MILESTONES ERA. Retrieved March 24, 2026, from <a href="https://www.acgme.org/globalassets/milestones-implementation-2020.pdf">https://www.acgme.org/globalassets/milestones-implementation-2020.pdf</a>',
   'Nasca, T. J., Philibert, I., Brigham, T., &amp; Flynn, T. C. (2012). The Next GME Accreditation System: Rationale and Benefits. <i>New England Journal of Medicine</i>, 366(11), 1051-1056. <a href="https://doi.org/10.1056/nejmsr1200117">https://doi.org/10.1056/nejmsr1200117</a>',
   'Schritz-Carroll, L. (n.d.). ACC&rsquo;15 Training Administrator Session. Retrieved March 24, 2026, from <a href="https://www.acc.org/-/media/Non-Clinical/Files-PDFs-Excel-MS-Word-etc/Membership/Cardiology-Training-and-Workforce-Committee/Presentations/Training-Admin-Sessions/Coordinator-Job-Description-National-Task-Force.pdf">https://www.acc.org/-/media/Non-Clinical/Files-PDFs-Excel-MS-Word-etc/Membership/Cardiology-Training-and-Workforce-Committee/Presentations/Training-Admin-Sessions/Coordinator-Job-Description-National-Task-Force.pdf</a>',
   'Common Program Requirements. (n.d.). Www.acgme.org. <a href="https://www.acgme.org/programs-and-institutions/programs/common-program-requirements/">https://www.acgme.org/programs-and-institutions/programs/common-program-requirements/</a>',
   'Edgar, L., Roberts, S., &amp; Holmboe, E. (2018). Milestones 2.0: A Step Forward. <i>Journal of Graduate Medical Education</i>, 10(3), 367-369. <a href="https://doi.org/10.4300/jgme-d-18-00372.1">https://doi.org/10.4300/jgme-d-18-00372.1</a>',
 ],
 "acknowledgements": [
   "Special thank you to Lisa Schritz, C-TAGME and her role in the success of the CDTF",
   "Special thank you to all the members of the CDTF",
   "Special thank you to Laura Edgar, Vice President of Milestones, ACGME",
   "Extra special thank you to Ruth Nawatiak, C-TAGME who has been my personal mentor for going on decades.",
 ],
},
]

# ---------------------------------------------------------------- rendering

def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "h2":
            out.append(f"      <h2>{val}</h2>")
        elif kind == "h3":
            out.append(f"      <h3>{val}</h3>")
        elif kind == "p":
            out.append(f"      <p>{val}</p>")
        elif kind == "ul":
            items = "\n".join(f"        <li>{i}</li>" for i in val)
            out.append(f"      <ul>\n{items}\n      </ul>")
        elif kind == "ol":
            items = "\n".join(f"        <li>{i}</li>" for i in val)
            out.append(f"      <ol>\n{items}\n      </ol>")
        elif kind == "olA":
            items = "\n".join(f"        <li><strong>{a}</strong> {b}</li>" for a, b in val)
            out.append(f'      <ol class="actions">\n{items}\n      </ol>')
        elif kind == "fig":
            cls = f' class="{val["cls"]}"' if val.get("cls") else ""
            out.append(f'      <figure{cls}>\n'
                       f'        <img src="{val["src"]}" alt="{val["alt"]}" loading="lazy" decoding="async">\n'
                       f'        <figcaption>{val["caption"]}</figcaption>\n'
                       f'      </figure>')
        elif kind == "tbl":
            out.append(f'      <div class="tbl-wrap">\n      {val}\n      </div>')
    return "\n".join(out)


def render_authors(a):
    multi_aff = len(a["affiliations"]) > 1
    multi_auth = len(a["authors"]) > 1
    if multi_auth and multi_aff:
        names = ", ".join(f'{x["name"]}<sup>{x["aff"]}</sup>' for x in a["authors"])
        affs = " &nbsp;&middot;&nbsp; ".join(f'<sup>{i+1}</sup> {t}'
                                            for i, t in enumerate(a["affiliations"]))
    else:
        names = ", ".join(x["name"] for x in a["authors"])
        affs = " &nbsp;&middot;&nbsp; ".join(a["affiliations"])
    return names, affs


def citation(a):
    """No volume: FULGME publishes issues only, so the volume slot is omitted,
    which is the standard form. The article identifier (A1..A5) replaces the
    page range, because each article PDF is separately paginated from 1 and the
    previously printed ranges did not resolve to real pages."""
    doi = f'. DOI: {a["doi"]}' if a.get("doi") else ''
    return (f'{a["cite_authors"]}. {html.unescape(a["title"])}. FULGME. '
            f'{ISSUE["pub_iso"][:4]};({ISSUE["issue"]}):{a["id"]}{doi}')


def render_abstract(a):
    if a["abstract_structured"]:
        rows = "\n".join(f'      <dt>{k}</dt><dd>{v}</dd>' for k, v in a["abstract_structured"])
        return f'    <dl>\n{rows}\n    </dl>'
    return f'    <p>{a["abstract_plain"]}</p>'


def page(a, prev_a, next_a):
    names, affs = render_authors(a)
    url = f'{SITE}/{ISSUE["path"]}/{a["slug"]}/'
    pdf_url = f'{url}pdf/{a["pdf"]}' if a.get("pdf") else ""
    cite = citation(a)
    plain_title = html.unescape(a["title"])

    if a["abstract_structured"]:
        meta_abs = " ".join(f"{k}: {html.unescape(v)}" for k, v in a["abstract_structured"])
    else:
        meta_abs = html.unescape(a["abstract_plain"])

    scholar = "\n".join(f'<meta name="citation_author" content="{html.escape(html.unescape(x["name"]))}">'
                        for x in a["authors"])
    scholar += "\n" + "\n".join(f'<meta name="citation_author_institution" content="{html.escape(t)}">'
                               for t in a["affiliations"])

    # Buttons vary: back issues have no per-article PDF, some link out to a full text.
    btns = []
    if a.get("pdf"):
        btns.append(f'<a class="btn" href="pdf/{a["pdf"]}" download="{a["pdf"]}">'
                    f'<span aria-hidden="true">&#8681;</span> Download this article (PDF)</a>')
    btns.append(f'<a class="btn{"" if a.get("pdf") else ""} ghost" href="../pdf/{ISSUE["issue_pdf"]}" download>Full issue PDF</a>')
    if a.get("full_text_url"):
        btns.append(f'<a class="btn ghost" href="{a["full_text_url"]}" rel="noopener">'
                    f'Author&rsquo;s full version <span aria-hidden="true">&rsaquo;</span></a>')
    btns.append(f'<a class="btn ghost" href="../">All articles in {ISSUE["label"]}</a>')
    if not a.get("pdf"):
        btns[0] = btns[0].replace('class="btn ghost"', 'class="btn"')
    buttons = "\n    ".join(btns)

    doi_fact = (f'<div><dt>DOI</dt><dd><code>{a["doi"]}</code></dd></div>' if a.get("doi")
                else '<div><dt>DOI</dt><dd>Pending correction</dd></div>')
    doi_meta = (f'<meta name="citation_doi" content="{a["doi"]}">\n' if a.get("doi") else "")
    doi_info = (f'<div><dt>Article DOI</dt><dd>{a["doi"]}</dd></div>' if a.get("doi")
                else '<div><dt>Article DOI</dt><dd>Pending correction, see note above</dd></div>')
    reviewed = a.get("peer_reviewed", True)
    access_short = ("Peer reviewed, open access" if reviewed
                    else "Invited board contribution, not peer reviewed")
    access_long = ("Peer reviewed, open access, free to read" if reviewed
                   else "Invited board contribution, not peer reviewed, open access, free to read")
    corr_notice = (f'<div class="notice correction"><p><strong>Correction, {a["correction"]["date"]}.</strong> '
                   f'{a["correction"]["text"]}</p></div>\n' if a.get("correction") else "")
    ed_notice = ("" if reviewed else
        '<div class="notice"><p><strong>Invited board contribution.</strong> This article is part of the '
        'journal&rsquo;s annual invited special topic section. It was invited by the editorial board '
        'rather than submitted through the open call, and it is editorial content rather than '
        'peer-reviewed research. The author took no part in the decision to publish it. See the '
        '<a href="../../policies/#peer-review">peer review policy</a>.</p></div>\n')
    doi_notice = (f'<div class="notice"><p><strong>Note on this article&rsquo;s DOI.</strong> {a["doi_note"]}</p></div>\n'
                  if a.get("doi_note") else "")
    issue_note = (f'<div class="notice"><p><strong>About this issue.</strong> {ISSUE["note"]}</p></div>\n'
                  if ISSUE.get("note") else "")

    kickers = (f'<span class="kicker special">{a["special"]}</span>' if a["special"] else "")
    kickers += f'<span class="kicker">{a["type"]}</span>'

    refs = ""
    if a.get("references"):
        items = "\n".join(f'        <li id="ref{i+1}">{r}</li>' for i, r in enumerate(a["references"]))
        refs = f'\n      <section class="refs" aria-labelledby="refs-h">\n        <h2 id="refs-h">References</h2>\n        <ol>\n{items}\n        </ol>\n      </section>'

    ack = ""
    if a.get("acknowledgements"):
        items = "\n".join(f'          <li>{x}</li>' for x in a["acknowledgements"])
        ack = f'\n      <section class="ack" aria-labelledby="ack-h">\n        <h2 id="ack-h">Acknowledgements</h2>\n        <ul>\n{items}\n        </ul>\n      </section>'

    ld = {
        "@context": "https://schema.org", "@type": "ScholarlyArticle",
        "headline": plain_title, "name": plain_title,
        "author": [{"@type": "Person", "name": html.unescape(x["name"])} for x in a["authors"]],
        "abstract": meta_abs,
        "datePublished": ISSUE["pub_iso"],
        **({"identifier": f'https://doi.org/{a["doi"]}',
            "sameAs": f'https://doi.org/{a["doi"]}'} if a.get("doi") else {}),
        "url": url, "inLanguage": "en", "isAccessibleForFree": True,
        "license": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
        "copyrightYear": int(ISSUE["pub_iso"][:4]),
        "copyrightHolder": [{"@type": "Person", "name": html.unescape(x["name"])}
                            for x in a["authors"]],
        "pagination": a["id"],
        "isPartOf": {
            "@type": "PublicationIssue", "issueNumber": ISSUE["num"],
            "datePublished": ISSUE["pub_iso"], "url": f'{SITE}/{ISSUE["path"]}/',
            "isPartOf": {"@type": "Periodical",
                         "name": "FULGME: Forum for United Leaders in Graduate Medical Education",
                         "issn": ISSUE["issn"],
                         "publisher": {"@type": "Organization",
                                       "name": "Forum for United Leaders in Graduate Medical Education",
                                       "url": "https://www.fulgme.org"}},
        },
    }

    def cell(other, direction):
        if not other:
            return '    <div></div>'
        cls = "next" if direction == "Next" else "prev"
        return (f'    <a class="{cls}" href="../{other["slug"]}/">'
                f'<span class="dir">{direction} article &middot; {other["id"]}</span>'
                f'<span class="t">{other["title"]}</span></a>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{a["title"]} | FULGME Journal</title>
<meta name="description" content="{html.escape(meta_abs[:180])}">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="../../assets/journal.css">

<!-- Highwire citation tags: read by Google Scholar and indexing services -->
<meta name="citation_journal_title" content="FULGME: Forum for United Leaders in Graduate Medical Education">
<meta name="citation_journal_abbrev" content="FULGME">
<meta name="citation_publisher" content="Forum for United Leaders in Graduate Medical Education">
<meta name="citation_issn" content="{ISSUE["issn"]}">
<meta name="citation_title" content="{html.escape(plain_title)}">
{scholar}
<meta name="citation_publication_date" content="{ISSUE["pub_iso"].replace("-", "/")}">
<meta name="citation_issue" content="{ISSUE["issue"]}">
<meta name="citation_firstpage" content="{a["id"]}">
{doi_meta}<meta name="citation_abstract_html_url" content="{url}">
{f'<meta name="citation_pdf_url" content="{pdf_url}">' if pdf_url else ""}
<meta name="citation_fulltext_html_url" content="{url}">
<meta name="citation_language" content="en">

<link rel="icon" href="../../assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="../../assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="../../assets/apple-touch-icon.png">
<meta property="og:image" content="https://journal.fulgme.org/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://journal.fulgme.org/assets/og-image.png">
<!-- Dublin Core -->
<meta name="DC.title" content="{html.escape(plain_title)}">
<meta name="DC.creator" content="{html.escape(', '.join(html.unescape(x['name']) for x in a['authors']))}">
<meta name="DC.publisher" content="Forum for United Leaders in Graduate Medical Education">
<meta name="DC.date" content="{ISSUE["pub_iso"]}">
<meta name="DC.type" content="{a["type"]}">
<meta name="DC.identifier" content="{a["doi"] or ISSUE["issue_doi"]}">
<meta name="DC.rights" content="Open access. Copyright is retained by the author(s). Published under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International licence (CC BY-NC-ND 4.0).">
<meta name="DC.rights.uri" content="https://creativecommons.org/licenses/by-nc-nd/4.0/">
<link rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">

<!-- Social sharing -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="FULGME Journal">
<meta property="og:title" content="{html.escape(plain_title)}">
<meta property="og:description" content="{html.escape(meta_abs[:200])}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
</head>
<body>
<a class="skip" href="#article">Skip to article</a>

<div class="jbar">
  <div class="wrap">
    <a class="brand" href="../../"><img class="blogo" src="../../assets/fulgme-mark.png" alt="" width="91" height="94" decoding="async"><span>FULGME<span class="tm">TM</span> Journal</span></a>
    <span class="meta">{ISSUE["running_head"]} &middot; {ISSUE["published"]}</span>
  </div>
</div>

<nav class="crumb" aria-label="Breadcrumb">
  <div class="wrap">
    <ol>
      <li><a href="../../">FULGME Journal</a></li>
      <li><a href="../">{ISSUE["label"]}</a></li>
      <li aria-current="page">{a["id"]}</li>
    </ol>
  </div>
</nav>

<main class="wrap">
<article class="card" id="article">

  <div class="ahead">
    <p class="atop">{kickers}<span class="artid">{a["id"]}</span></p>
    <h1 class="atitle">{a["title"]}</h1>
    <p class="authors">{names}</p>
    <p class="affils">{affs}</p>
    <dl class="facts">
      <div><dt>Article type</dt><dd>{a["type"]}</dd></div>
      <div><dt>Published</dt><dd>{ISSUE["published"]}</dd></div>
      {doi_fact}
      <div><dt>Access</dt><dd>{access_short}</dd></div>
    </dl>
  </div>

  <div class="abar row">
{buttons}
  </div>

  <div class="abstract">
    <h2>Abstract</h2>
{render_abstract(a)}
  </div>

  <div class="abody">
{corr_notice}{ed_notice}{issue_note}{doi_notice}{render_body(a["body"])}
{refs}{ack}
    <p class="coi"><strong>Conflict of interest.</strong> {COI}</p>

    <div class="citebox">
      <h2>How to cite this article</h2>
      <p>{cite}</p>
      <button class="copy" type="button" data-cite="{html.escape(cite, quote=True)}">Copy citation</button>
    </div>

    <section class="ainfo card" aria-labelledby="ainfo-h">
      <h2 id="ainfo-h">Article Information</h2>
      <dl>
        <div><dt>Journal</dt><dd>FULGME: Forum for United Leaders in Graduate Medical Education</dd></div>
        <div><dt>Publisher</dt><dd>Forum for United Leaders in Graduate Medical Education</dd></div>
        <div><dt>ISSN</dt><dd>{ISSUE["issn"]}</dd></div>
        <div><dt>Issue</dt><dd>{ISSUE["num"]}, {ISSUE["published"]}</dd></div>
        <div><dt>Article number</dt><dd>{a["id"]}</dd></div>
        {doi_info}
        <div><dt>Issue DOI</dt><dd>{ISSUE["issue_doi"]}</dd></div>
        <div><dt>Journal DOI</dt><dd>{ISSUE["journal_doi"]}</dd></div>
        <div><dt>Access</dt><dd>{access_long}</dd></div>
        <div><dt>Copyright</dt><dd>Retained by the author(s)</dd></div>
        <div><dt>Licence</dt><dd><a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license">CC BY-NC-ND 4.0</a></dd></div>
        <div><dt>Contact</dt><dd><a href="mailto:info@fulgme.org">info@fulgme.org</a></dd></div>
      </dl>
    </section>

    <p class="licence"><strong>Copyright and licence.</strong> &copy; The author(s). This article is
    published open access under a
    <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
    International licence (CC BY-NC-ND 4.0)</a>. You are free to copy and redistribute it in any medium
    or format, with attribution to the author(s) and FULGME, provided you do not use it commercially and
    do not distribute altered versions.</p>
  </div>
</article>

<nav class="pager" aria-label="Article navigation">
{cell(prev_a, "Previous")}
{cell(next_a, "Next")}
</nav>
</main>

<footer>
  <div class="wrap">
    <p><a href="../../">FULGME Journal</a> &nbsp;&middot;&nbsp; <a href="https://www.fulgme.org">fulgme.org</a> &nbsp;&middot;&nbsp; <a href="mailto:info@fulgme.org">info@fulgme.org</a></p>
    <p class="legal">
      &copy; The author(s). Published by FULGME under
      <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license">CC BY-NC-ND 4.0</a> &nbsp;&bull;&nbsp;
      Issue {ISSUE["num"]}, {ISSUE["published"]} &nbsp;&bull;&nbsp; ISSN: {ISSUE["issn"]} &nbsp;&bull;&nbsp;
      Journal DOI: {ISSUE["journal_doi"]} &nbsp;&bull;&nbsp; Issue DOI: {ISSUE["issue_doi"]}
    </p>
  </div>
</footer>

<script type="application/ld+json">
{json.dumps(ld, indent=2)}
</script>

<script>
document.querySelectorAll('.copy').forEach(function (btn) {{
  btn.addEventListener('click', function () {{
    var text = btn.getAttribute('data-cite');
    var original = btn.textContent;
    function done(msg) {{ btn.textContent = msg; setTimeout(function () {{ btn.textContent = original; }}, 1800); }}
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(text).then(function () {{ done('Copied'); }}, function () {{ done('Press Ctrl+C'); }});
    }} else {{
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', '');
      ta.style.position = 'absolute'; ta.style.left = '-9999px';
      document.body.appendChild(ta); ta.select();
      try {{ document.execCommand('copy'); done('Copied'); }} catch (e) {{ done('Press Ctrl+C'); }}
      document.body.removeChild(ta);
    }}
  }});
}});
</script>
</body>
</html>
"""


if __name__ == "__main__":
    # Paths resolve relative to this script, so it works from the repo root.
    HERE = pathlib.Path(__file__).resolve().parent
    root = HERE / ISSUE["path"]
    for i, a in enumerate(ARTICLES):
        d = root / a["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            page(a, ARTICLES[i - 1] if i > 0 else None,
                    ARTICLES[i + 1] if i < len(ARTICLES) - 1 else None), encoding="utf-8")
        print("wrote", d / "index.html")

    urls = [(f'{SITE}/', "monthly", "1.0"), (f'{SITE}/{ISSUE["path"]}/', "yearly", "0.9")]
    urls += [(f'{SITE}/{ISSUE["path"]}/{a["slug"]}/', "yearly", "0.8") for a in ARTICLES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, freq, pri in urls:
        sm += ["  <url>", f"    <loc>{u}</loc>", "    <lastmod>2026-08-17</lastmod>",
               f"    <changefreq>{freq}</changefreq>", f"    <priority>{pri}</priority>", "  </url>"]
    sm.append("</urlset>")
    (HERE / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    print("wrote sitemap.xml with", len(urls), "urls")
