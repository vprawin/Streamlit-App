import streamlit as st
import cohere
# Title for the app
st.title("Chatbot")

# Input box
user_input = st.text_input("Enter the Question:")

# Button to process the input
if st.button("Process"):
    
    # Set your API key
    co = cohere.Client("aGEw4etYOyl29QgrQ3vpPcaw4U0XRK2FODsFWPon")

    # Define context and question
    context = """
    1. We solve all your building maintenance challenges Quickly, Affordably, and Efficiently FM-made simple IEM simplifies the complexity of facilities management, allowing you to easily control the risks and turn your buildings into business enhancers. We specialize in redefining estates from mere cost centers to pivotal business enablers. With extensive expertise in facilities management, we empathize with the challenges of accountability in the absence of streamlined processes. We recognize the burden of risk management overshadowing opportunities for meaningful business impact.


    2. Business impact. What We Do
    BUILDING PROJECTS
    We carry out all aspects of building projects, from design to delivery, to handover
    TECHNICAL CONSULTANCY
    We provide technical consultation and support, across all aspects of your estate
    PLANNED AND REACTIVE MAINTENANCE
    We deliver hard services, covering planned, remedial, and reactive maintenance, specializing in compliance.

    3.   Why work with IEM?
    NO CONTRACT
    No long-term obligation
    We are only as good as our last job Gives you a flexible solution with no fixed-term commitment
    FREE CAFM SYSTEM
    Reduces Costs Centralised Maintenance Control and Compliance documentation management
    Total visibility in one place
    REGIONALISED SUPPLY CHAIN
    Timely and quick response times
    More efficient sustainability
    Supporting local contractors


    4. Supporting local contractors
    COMPANIES WE HAVE PROUDLY SERVED INCLUDE:
    Client Chatham House
    IVC Evidensia
    Stonegate Pub Company
    Bvlgari
    Logo Cox Automotive Brand Font Vector Graphics Png Favpng
    Nhs  1
    Knightsbridge  Blue
    Dough And Co
    Arnold Clark
    Rockhurst
    Motorpoint
    Quills Group
    
    
    5. How facilities management can future-proof your business
    Strategic facilities management is a powerful tool for those that know how to use it. For many businesses, estate management is often reactive and fails to develop assets and add value to portfolios.
    
    The global pandemic has been hugely disruptive in the field of estate management. First, many premises were abandoned – virtually overnight – for an unknown period of time. Now, as we plan a return, organisations are having to make drastic changes to the way they use their sites in order to keep staff safe. Designing resilience into assets can not only protect them but aid the organisation as a whole.
    
    This must start with an in-depth understanding of the estate, it’s strengths and its weaknesses. For many, hard elements of FM have been hugely challenging over the previous months since they are designed to function with the building at near full capacity.
    
    Failure to manage this situation can result in a lack of compliance. At worst, this can lead to dangerous health outcomes as was seen with an outbreak of Legionnaires’ disease earlier this year. Understanding risk allows potentially costly and hazardous problems to be avoided.
    
    Once the fundamental needs of the organisation are met by its estate, attention can be turned to increasing the value of assets. Sites and premises should be viewed in terms of their potential. The upkeep of under-utilised sites is a resource drain.
    
    Instead, these areas should become a focus for redevelopment. Real estate should add value to the organisation through by enhancing the safety and productivity of a site.. Portfolio optimisation is a key way of financially streamlining an organisation, providing a buffer for unexpected spends or greater potential for investing into development.
    
    An area garnering increasing attention is the creation of a workplace that supports the productivity and wellbeing of employees. Future-proofing is about embracing change. The way we work will continue to evolve, especially as we continue to recover from the pandemic.
    
    Spaces should be designed to allow for agile working and changes in working style. The most flexible thing in a space is never the furniture, nor the walls. It’s the people. Space should encourage movement, creative work, and facilitate safety.
    
    The space should also reflect and encourage a strong workplace culture. A close-knit workplace culture is important for keeping staff motivated and engaged even when times are difficult. Staff that feel supported and at home in their workplace will be more loyal.
    
    Finally, the sustainability of the workplace will be under ever greater scrutiny in the coming years. With many of the greatest challenges business face, including the global pandemic, traced back to unsustainable practices, the pressure will be on everyone to do better.
    
    Estate managers can save on costs and improve the reputation of an organisation by implementing sustainable practices. From insulation and waste disposal to buying furniture made of more eco-friendly material, the possibilities are endless.
    
    The role of the estate manager is both to be a creative problem solver and a visionary for the potential of the portfolio. Those with a strong understanding of estate management and how it aligns with the organisation’s priorities have a powerful tool at their fingertips.
    
    
    5. Meet the Team: Alistair Scott
    What is your role at IEM and what does it involve day to day?
    I am responsible for the day-to-day operations of the company and all the technical support elements. This involves making sure the team have the right tools, equipment and support to do a great job. By doing this, the team are then enabled to get the best out of themselves. I don’t like micro-management, so I like to agree success criteria up-front with the team and then allow them to do it their way.
    
    I enjoy getting involved in the fulfilment of the large technical projects and ensuring they are executed correctly, to a high standard and on time. A lot of my time is also spent on maintaining and growing client relationships, ensuring the customer experience is always to a high standard.
    
    How did you find your way into estate management? (Tell us a bit about your background)
    I was trained as an engineer in the military. Concurrently, this is where I grew as a leader, deploying and leading teams when training or in operation. This taught me how to lead, manage, and develop a diverse group of individuals. I molded them into a highly effective team that was capable of delivering a variety of complex projects on a timely basis and across a variety of environments.
    
    It doesn’t surprise me that there are a lot of ex-military personnel working in facilities management as there are many traits that are similar.
    
    I got involved initially from the engineering angle, as I understood electrical, mechanical, and electronic systems. On top of that, I had the leadership competency to put people in the right place, with the right piece of equipment to do the job first time….which at the end of the day is facilities management.An estate manager using a tablet during a site visit
    
    What is your favourite thing about your job/the industry?
    I absolutely love what I do. What really excites me is that no two days are the same. It’s a really diverse industry when it comes to all the different problems that come up on a daily basis. Therefore, you're constantly thinking and challenging yourself. It keeps your brain moving and allows you to stay engaged. You naturally feel ecstatic when you do something good for someone. We're not going in and smashing the place up, we're going in to make things work, adding value to businesses and buildings and landlords. For me, this is really exciting and my favourite part of the job.
    
    How could the industry be improved?
    The biggest challenge we’ve faced as an industry is people’s perspective of us, and their understanding of what we offer. However, I think we’ve already started seeing improvements in this area. Years ago, businesses went to large FM companies to do everything for them. Now, companies are realising that having the right people with the right skill set within the facilities management sphere, is more of a benefit than just going to a general FM provider. It's like the high street, people are flocking back to local butchers or bakers because it’s more personal and better quality. FM is no different, people like going to specialists within their field but they also want that personal touch.
    
    What are your key predictions for/the biggest issues facing the estate management industry over the next year?
    Technology is really being pushed and for the right reasons. However, I have on a few occasions added a cautionary warning into going down this route. Overall, I really like IOT, especially if utilised correctly. It can give you plenty of warning if things go wrong, telling you if something’s going to fail, and can be really useful for a range of services. However, it’s important we still remember the basics and not rely heavily on technology. A trend I’m seeing is technology taking so much of the limelight that the fundamentals are being forgotten. As much as advancements in technology is a good thing, the basics can’t be forgotten. It all links back to simplicity, you don’t always need lots of advanced equipment and the latest tech, just the right tools and the right people.
    
    What is your biggest passion/favourite hobby outside of work?
    A Formula 1 car on the race trackI am a massive motor-sport fan. I follow all genres and types, whether it be road cars, British Touring Cars, or Formula 1. I am also heavily involved with amateur race driving and even motorbikes. If it’s motorized and fast, I love it.
    
    Gone are the days I really get involved in the tinkering element, but the driving experience and that team ethic of everybody in a team working towards a common goal, as well as achieving that goal on time, is what I still love and have taken into the business arena.
    
    My other major passion is cooking. For me there is nothing more relaxing than cooking a meal for family and friends, with everyone sitting around a table on weekends, chatting and enjoying the experience. These are those special moments that we missed during Covid times, that I can’t wait to start doing again.
    
    6. Why support for facilities managers is essential as buildings reopen
    One of the side effects of the pandemic, working from home and the workplace revolution is that we all have a greater appreciation of the impact of buildings on our mental health and wellbeing. But what about the mental health of those charged with managing buildings as they reopen?
    
    Many businesses may look to adopt a hybrid work model post-pandemic, but the reality is that most buildings are on track to be fully reopened in June when the Covid restrictions end. Many of these spaces have been dormant or below occupancy for more than a year and compliance might have fallen by the wayside.
    
    Ensuring buildings are safe to reopen is not just about cleaning and hygiene. It’s about ensuring that all aspects are compliant, and that duty falls to estate managers. That level of accountability is a big burden and will undoubtably be the cause of much stress for those individuals.
    
    An anxious return?
    
    It’s quite clear that the onus is on employers to help building occupants feel supported in their mental health, and estate managers have a big role to play.
    
    There will be plenty of people that are excited to get back to the office, but there will be just as many that are anxious about the return.
    
    Business leaders too will be anxious. They want to ensure the safety of their employees, clients, and customers. They also have a financial risk to consider. If a building fails compliance, that might lead to a fine or the space being shut down. That could be highly disruptive to the business.
    
    Estate managers must manage these risks and communicate with leadership and building users how and when they have been mitigated. It’s a big weight to carry and we businesses must ensure that their estate managers have the support they need – not just through the tools they need to do their jobs, but on the wellbeing side too.
    
    Supporting estate managers
    
    Estate teams should already be working in close consultation with other senior leaders. Since the pandemic struck and the role of the building was amplified, many estate managers have found themselves to have an elevated voice in the business. Now is the time to capitalise and ensure that this remains the case long after the pandemic.
    
    Estate managers should share how and why they are managing various tasks, from compliance to lighting, and water safety to energy management. For their part, business leaders must do all they can to support them in achieving their goals.
    
    This could include the creation of an up-to-date asset list; an audit of building condition; compliance inspections and assessments; prioritising projects; and the delivery itself.
    
    This can be a hugely demanding workload for a team, let alone a one-man band. In many cases it can be beneficial to partner with an expert consultant to help manage one of more areas of estate management. Business leaders can support their teams by being open to this option.
    
    This is not just a ‘nice to do’. This is essential in supporting the mental health of estate managers, and in turn the business.
    
    We offer a range of estate management services that will support your business and its employees. Contact us today to discuss how we can support your estate management.
    
    
    7.  IEM founder Alistair Scott bids to join IWFM board
    IEM founder Alistair Scott has nominated himself to join the board of the Institute of Workplace and Facilities Management (IWFM). The IWFM, formerly the British Institute of Facilities Management, was formed in 1993 and exists to “promote excellence among a worldwide membership community of around 14,000 and to demonstrate the value and contribution of workplace and facilities management more widely”.
    
    The IWFM board consists of 13 members, six of which are volunteers who must hold professional membership within the Institute. Alistair has applied for the role of non-executive director as he hopes to use his extensive experience to help the board meet and exceed its objectives.
    
    Voting is now open. All members of the IWFM at member grade and above are eligible to vote and we’d love your support – you can vote for Alistair here.
    
    Alistair Scott’s candidate statement
    I am a certified mechanical, electrical and electronic engineer and have more than 25 years’ experience in technical engineering and senior facilities management roles. Throughout my career I have witnessed the good and the bad of facilities management, as well as seeing many opportunities for improvement. Through my experience and expertise, I truly believe that I can add significant value to the IWFM organisation.
    
    As the founder of my own FM company, Integrated Estate Management, I am fully aware of the need for strong strategic direction, setting and measuring objectives, and astute financial management. My engineering and military background has given me excellent leadership skills to complement the business acumen that I have developed in the last two decades.
    
    I look forward to taking an active role on the board, sharing my expertise and helping to drive the IWFM towards its objectives. I have held numerous board positions and operated across multiple industries, including the following companies, Gatwick Airport, BAA, Liquid Capital and AkzoNobel (ICI) and Cloudfm. I understand the commitments and responsibilities that come with being a board member and am ready to support the IWFM.
    
    I have a distinct passion to make this industry more appealing, simple to understand and desirable to work in. Recognition of the facilities management sector has grown tremendously in the last 18 months, and I believe we must capitalise on this opportunity.
    
    The IWFM has a vital role in this, and I am excited to play my part.
    
    I am actively engaged in the industry and am always looking for ways to promote FM. As an FM coach and mentor, I have heard many of the concerns and frustrations from people within the industry and am looking forward to working on the board to improve the industry and add value.
    
    I am also involved with the Women in Construction organisation and share my expertise with the industry through comments and articles in leading trade titles such as Facilitate, FMJ and iFM.
    
    I ask for your vote so that I can support the IWFM as it enters an exciting new era.
    
    Vote for Alistair
    If you are an IWFM member, please cast your vote for Alistair.
    
    
    8. The future is bright; the future is simple
    Facilities Management shouldn't be this complicated!
    
    When IEM was founded, we did not want to perpetuate the confusion and complexity often associated with FM, so we made the decision to keep things simple.
    
    There were various reasons for this thinking, but the most important of these was the bad reputation that the industry had acquired, mainly due to its somewhat chequered history.
    
    According to Reuters, one of the primary reasons FM businesses have struggled in recent years (Carillion and Interserve spring to mind) is the continuous hamster wheel of signing long fixed-rate contracts at un-sustainable pricing.
    
    Complicating the services offered to clients makes it easier to hide the real cost and mask the value customers are getting.
    
    Simplifying complexity is a skill that most great businesses and leaders possess, but it is sometimes missing in FM.
    
    "Simple can be harder than complex. You have to work hard to get your thinking clean, to make it simple. But it's worth it in the end, because once you get there you can move mountains" Steve Jobs
    
    As the world becomes smaller, the ease with which businesses can get information into the marketplace becomes even easier. However, the need for quality content that stands out becomes ever more necessary.
    
    Selling service-driven products is challenging, especially in a world of so much noise, quality content and competition. When trying to justify a price-point, expensive complex products are usually perceived as more merited than simple ones.
    
    Successful organisations and leaders are highly skilled in simplifying this complexity, instead of "complexifying” simplicity.  However, if you get it wrong, this can confuse your customers, who nod their heads politely but have no clue how you will ease their pain points.
    
    Clarity and simplicity
    
    "If you can’t explain it simply, you don’t understand it well enough" Albert Einstein
    
    Any industry focused on selling to the lowest bidder will always have underlying challenges, especially if that industry relates to services. The way many businesses overcome this issue is through "Bundling" or giving perceived value. After all, it is easy to compare apples with apples (hourly rate of jobs, materials and length of time) but much harder to compare the more subjective elements (quality, management fees and administrative support.)
    
    FM has always been an industry famous for its acronyms and hidden costs; that’s why there is a need for clarity and a much more simplistic approach. Good FM companies will sell real features and services that customers genuinely need, rather than perceived value, due to "Bundling" features that clients will never use.
    
    One of the main challenges the FM industry has had, is that they have to come in at the lowest price and give the perception of more added value. The FM industry needs to understand the power of clarity and simplicity.
    
    When building a sustainable business, concepts, jargon and complex features should never be at the expense of customer benefits.
    
    The next few years should bring a shift from the complicated world of hidden features and acronyms that nobody understands, to a drive for removing complexity and replacing it with simplicity.
    
    The Future is bright
    
    Outsourced providers will need to add more value than before. Increased spending budgets to get businesses up and running as soon as possible will create more business opportunities.  FM companies that can adapt quickly, focus on the basics, without the bells and whistles, whilst helping customers prioritise, are the most likely to flourish and grow.
    
    Other reasons why 2021 will be bright for the FM industry include:
    
    Cost reduction may be necessary, but organisations will also need to free up more funds to get their estates trading in super-fast time.
    With many buildings closed for so long, there will need to be urgent investments in Health and Safety, including compliance checks.
    FM/Property Managers will suddenly have more exposure and be at the forefront of strategic decision making.
    IoT and AI advances will make the industry sexier, especially the drive towards predictive and preventative maintenance - however, this may need to be put on hold for a short while, as businesses open safely and get their basics right first.
    Employees will probably want to get back to their workplaces and interact face to face with their work colleagues once more, and this will be a crucial part of facilities teams’ activities over the Spring and Summer months.
    There will be a level of urgency not seen for many years, so the demand for services will be very high.
    If FM companies get things right and make it easier for customers to attain more value, the next 12-24 months could be one of the most exciting times in history for the industry. Getting estates up and running in a post-covid world, will bring many opportunities for FM businesses to grow and for clients to build workplaces that will be business enhancers, not just cost centres.
    
    We were set up with the goal of simplifying estate management. Contact us today to discuss how we can support your business.
    
    9. 5 key considerations for facilities management when reopening a building
    The current lockdown means that many workplaces have become vacant again, or at the very least continue to be vastly under-occupied. Though it may feel like a return to normal is a long way off, estate and facilities managers must prepare now for that time.
    
    When the restrictions do ease, a lot of businesses may see a clamour from employees who want to get back to their place of work. This process cannot be rushed and estate managers have a vital role to play in ensuring that a workplace is ready to be occupied again.
    
    There are of course numerous things to consider to get a workplace ready to reopen. Here are five of the most important.
    
    Hygiene
    This may seem obvious, but it’s absolutely critical to stay on top of hygiene. This includes keeping updated with the latest information from the Government and health bodies, as well as implementing strong hygiene processes at a site. Estate managers should act as a key consultant to organisations. Even though we are ten months into the pandemic, it cannot be assumed that all building occupants will know or follow the best hygiene practices, so signage and consistent communication with all occupants is a must.
    HVAC
    We know that the virus is increasingly airborne. HVAC systems must be assessed and adapted to ensure that they provide a strong defence against airborne transmission. This can include the type of air filters used, the frequency they are changed and the percentage of outside air pumped into a building. Where possible, windows should be left open to increase ventilation.
    Compliance
    Compliance covers everything from fire risk to electrical, and legionella to asbestos. In buildings that have spent any time vacant or with reduced occupancy, it’s highly likely that checks will need to be made before full occupancy to avoid both fines and health and safety breaches. Take water systems, for example. Many are designed under the assumption of regular flushing due to full a site being fully occupied. Times of irregular flushing can provide an opportunity for bacteria to flourish, which in the worst case scenario can lead to an outbreak of legionella. Estate managers should assume nothing is compliant as they prepare a site for reopening.
    Asset management
    Even the most up-to-date asset registries will need going over with a fine tooth comb ahead of a building reopening. It’s likely that the condition of many assets will have changed in the last year. For businesses without an understanding of its assets and their condition, this represents an opportune time to carry out an in-depth survey. This will also be an important step in ensuring compliance.
    Project management
    The sheer numbers of estate management tasks can be daunting for even the most experienced estate managers, let alone for small and medium sized businesses that may not have the in-house resources to cope. It’s worth partnering with a project manager to handle the process. The expertise is invaluable and any money spend will be made back many times over in workplace optimisation and the avoidance of fines for breaches of compliance.
    
    The IEM team is here to help you manage your estate. Whether you need a range of services, project management or simply a chat about how to transform your estate into a business enhancer, we can help out. Check out our Five Point Plan or contact us to find out more.
    
    
    10.  How to make facilities management simple and effective
    Facilities management, at its heart, is about looking after things. It is a vast role and may appear inherently complex, but it does not need to be difficult. By simplifying each of the elements of estate management, it is possible to create a streamlined and cohesive approach.
    
    For many, the instinct is to outsource to a large facilities management (FM) organisation with expertise in estate management. However, this isn’t an option for many smaller and mid-sized companies.
    
    Yet opting for the cheapest option on the market risks shelling out for a service that doesn’t do justice to the estate. For those managing their estate themselves, it can feel like an overwhelming challenge just to meet compliance measures and the time and resources this requires can distract from transforming the estate into a genuine business asset.
    
    In virtually every sector, organisations are looking to simplify and streamline their processes. This is possible with estate management too. By breaking the process down, it becomes easier to address each of the core elements of management, meet key targets, and understand priorities.
    
    Understanding what assets an estate possesses should be the key objective of an estate manager. Location, condition, life span, and economic value should all be identified. This should then be followed by a more in-depth investigation into the condition of those assets. Here, risks can be identified and precautions taken.
    
    Ensuring compliance is vital in any estate; non-compliance can come with unplanned costs and long-term damage to reputation. An understanding of asset condition allows compliance requirements to be met.
    
    From here, an organisation is in a position to plan for the future, begin forecasting capital expenditure and planning for tenders. A five-year plan can be produced with key compliance and business critical remedials prioritised according to risk. Finally, improvements and projects can go ahead, be they adjustments and refurbishment or major upgrades.
    
    By creating a step-by-step process, each element of estate management becomes manageable and vital aspects won’t be overlooked. Once your organisation understands precisely which areas of the estate need work and what needs doing, you are in a much better position to look for the best experts for the job. Simplifying the process makes it both transparent and accessible.
    
    While the remit of estate management is extremely broad, it is an opportunity to take a holistic view of the organisation’s assets. Once the process has been demystified, it can be an opportunity to build on what the organisation has in order to create an estate that reflects the business culture and feels like a home for its people.
    
    Excellence in estate management requires strategic thinking and continuous evaluation of the estate. For those new to this approach, there is a big learning curve, but streamlining the process makes it accessible to all.
    
    
    11. About IEM
    At IEM, our primary objective is clear: to transform inefficient spaces into productive environments, optimising your buildings to support your strategic goals.
    
    Say goodbye to cost centres and hello to business enablers with IEM's innovative approach to facilities management.
    
    We understand the frustrations of navigating the risks and everyday challenges of estate management, which can detract from your ability to contribute positively to your business.
    
    Integrity, reliability, simplicity, and transparency are the cornerstones of our approach.
    
    CONTACT US today to discover how we can streamline your facilities management processes.
    
    As facilities management experts, we extend our services to include project delivery, regardless of whether we provide the ongoing services or not.
    
    12. THE IEM STORY
    Alistair Scott, the driving force behind IEM, brings over 25 years of experience in technical engineering and senior facilities management roles. A certified mechanical, electrical, and electronic engineer, Alistair's journey began in the British Army, where he served for 14 years within the Royal Electrical Mechanical Engineers (REME), rising to the rank of Captain. During his military service, Alistair excelled as a mechanical aircraft technician, ultimately attaining the esteemed position of Engineering Officer. Transitioning from the military to the civilian sector, Alistair embarked on a global career in the facilities management (FM) industry. He held pivotal board positions at renowned organizations such as Gatwick Airport, BAA, Liquid Capital, and AkzoNobel (ICI), gaining invaluable insights and expertise along the way. Driven by a passion to revolutionise the FM industry and frustrated by its unnecessarily complex nature, Alistair founded IEM. With a commitment to simplifying processes and making a meaningful difference, Alistair leads IEM in its mission to deliver innovative, efficient, and sustainable facilities management solutions.
    "I have worked in senior FM roles across numerous industries and the common factor in them all was the daily complexity. I believe that facilities management should be simple to understand and deliver - that's why I founded IEM. I want to help organizations better understand their buildings, have more control over them and transform their estates into business enhancers."
    
    13.
    Our work
    IEM was founded to make facilities management simple, transparent and effective. To achieve this, we created our Five Point Plan. The plan covers end-to-end facilities management: Know your assets;
    Understand your condition;
    Control your compliance;
    Package your priorities;
    Manage your delivery.
    The plan can be tailored to meet your exact requirements – we can work on one or all five points with you. Find out more about our Five Point Plan. We have a nationwide network of certified engineers that have expertise in every facet of estate management, including electrical, mechanical, water systems, compliance, lighting and HVAC. See the full list of services we offer on our services page. IEM has experience in a range of sectors, including commercial, retail and warehousing. See the full list of our sectors here.
    
    Scottys little Soldiers
    Visit Scottys little Soldiers Website
    Care After Combat
    Mission Motorsport
    IWFM
    Veterans Can
    Bronze Military Covenent
    
    14. ACCREDITATIONS
    
    IWFM
    Safe Contractor Approved
    Gold With Dark Font Transparent1
    BESA Associate PNG
    Qualitas IMS 45001 Certified  (1)
    Qualitas IMS 9001 Certified
    Qualitas IMS 14001 Certified
    Principal Safety
    Best Company to work For "FM awards2024"
    
    15. Five Point Plan
    The plan is designed to be flexible and to fit your needs. You can pick and choose which elements you want IEM to help with and we'll work seamlessly with in-house services and other contractors.
    
    1. Know Your Assets
    According to Compare Soft, an effective asset register can have an impact on your revenue and cash flow by 5 – 18 per cent. We identify your assets and their location, condition, life span and economic value. We leave no stone unturned in creating an up-to-date register.
    Identify assets and location
    Condition
    Life span
    Economic value
    
    2. Understand Your Condition
    Evaluating the condition of an estate is a daunting prospect. We survey your buildings, identify construction and repair requirements, identify any risks and collate the data into a user friendly report.
    Survey your buildings
    Identify construction and repair condition
    Identify your risks
    Collate data
    
    3. Control Your Compliance
    The cost of health and safety fines is routinely higher than the cost of compliance. Businesses also have a duty to protect their employees and customers. We assess your current compliance position, check it against the latest legal guidance, carry out compliance inspections and categorise remedial and improvement actions. The end result is you will be fully compliant and have an easy way to manage compliance moving forwards.
    
    Assess current compliance position
    Legislative guidance
    Compliance inspections
    Categorise remedial and improvement actions
    
    4. Package Your Priorities
    With a full understanding of your estate, we’ll work with you to identify and address your priorities. This includes producing a plan for up to five years ahead, forecasting CAPEX expenditure, balancing priorities versus statutory requirements and assisting with tender production.
    
    Produce a 1-5 year plan
    Forecast your CAPEX expenditure
    Organise priorities overlayed against statutory requirements
    Tender production
    
    5. Manage Your Delivery
    We can take the lead role in delivering your program across one or multiple sites. We also offer construction, design and management support and deliver major upgrades and refurbishment work through our 2,500 strong nationwide network of engineers.
    
    
    Programme or project
    
    CDM support
    
    Individual or multi-site discipline delivery
    
    Deliver major upgrades and refurbishment works
    
    
    
    6. Frequently Asked Questions
    What is facilities management?
    Facilities management encompasses every aspect of a property, including electrical, water, lighting, health and safety, maintenance and compliance. It's also commonly referred to as estate management.
    
    Are your contractors certified and monitored?
    Does IEM just do repairs?
    IEM deliver all aspects of total building maintenance from planned, reactive to technical projects.
    
    Do you offer 24-hour (24/7) support?
    Yes, we are available 24/7, feel free to call any time for assistance and support
    
    Why did you come up with "The 5-point plan"?
    IEM was created in order to simplify the complexity of estate management, the 5-point plan is the framework that underpins our philosophy
    
    Why does IEM believe simplicity (removing the complexity) is so important?
    Through our extensive estate management experience, we identified that the complexity within maintaining a building leads to in-action, frustration and risk.
    
    Why is facilities management important?
    There are numerous benefits to effective facilities management. It is essential to remain compliant across all facets of an estate to avoid fines and to ensure that all occupants are safe while on the premises. Strong estate management practices can also transform a property from a risk to an asset. A well maintained estate can also be a big driver towards creating a productive working environment.
    
    What services do IEM provide?
    We provide every element of estate management, from asset management through to programme delivery. We have a nationwide network of more than 2,500 engineers that can be called upon at a moment’s notice to carry out any job.
    
    Can I pick and choose what services I need from IEM?
    Absolutely. You can engage us for our entire Five Point Plan or we can tailor a unique plan just for your estate. We will work seamlessly with your in-house team or other contracted services.
    
    How much does facilities management cost?
    This can vary depending on the size of your estate and the services you require. Contact us to find out more.
    
    Tel: 0203 772 4188
    info@integrated-em.com
    
    31, Facilities management services
    REACTIVE AND PROACTIVE MAINTENANCE
    
    At IEM, we specialise in both reactive maintenance to swiftly address immediate issues and proactive maintenance strategies to keep your facilities operating smoothly. Whether you need urgent fixes or planned preventive maintenance (PPM) to prevent future problems, we have the expertise to meet your needs. What sets us apart is our commitment to delivering these services with simplicity, transparency, and a personal touch that distinguishes us from larger FM providers.
    
    PROJECTS & MANAGEMENT
    
    In addition to our maintenance expertise, we excel in project delivery and estate management solutions. Whether it's overseeing minor repairs, executing PPM schedules, or managing extensive estates, count on IEM to handle it with precision and care.
    
    STRAIGHTFORWARD APPROACH
    
    We believe in straightforward communication and transparent processes. At IEM, we're not just service providers; we're proactive partners dedicated to maximising the efficiency and longevity of your facilities.
    
    107 (1)
    SECTORS
    With extensive industry experience, IEM efficiently handles a wide array of facilities tasks. From healthcare to education and retail, our expertise ensures seamless management of your facilities management program.
    Iem Sectors
    SERVICES
    Disciplines - Planned & Reactive
    Artboard 1
    Electrical & Mechanical
    Artboard 2
    Refrigeration
    Artboard 3
    Asbestos Management and Removal
    Artboard 4
    Plumbing Waste and Drainage
    Artboard 5
    Lighting LED Roll-outs & Design
    Artboard 6
    Civils
    Artboard 7
    Fire Systems & Risk Assessments
    Artboard 8
    Roofing
    Artboard 9
    Water Risk Assessments and Legionella
    Artboard 10
    Fit outs and Construction
    Artboard 11
    HVAC (Heating, Ventilation & Air-Conditioning)
    Artboard 12
    Intruder Systems and CCTV
    Artboard 13
    LEPC (Lifts, Escalators & Passenger Conveyors)
    Artboard 14
    Roller Shutter & Automatic Doors
    Artboard 15
    Utilities Connections (Gas, Electric, Water)
    Services Map
    Support Services
    Artboard 16
    Health and Safety Management
    Artboard 17
    CDM
    Artboard 18
    Listed Buildings & Conservation Area
    Artboard 19
    Principal Designers
    Artboard 20
    Main Contractor
    Artboard 21
    Tender Production & Support
    Artboard 22
    Dilapidation Support & Assessments
    Artboard 23
    ESOS
    Artboard 24
    Energy Management
    
    """
    question = user_input
    # Combine context and question
    input_text = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    
    # Generate text
    response = co.generate(
        model="command-xlarge-nightly",
        prompt=input_text,
        max_tokens=100
    )
    
    # Print the response
    #print("Answer:", response.generations[0].text)
    
    st.success(response.generations[0].text)
