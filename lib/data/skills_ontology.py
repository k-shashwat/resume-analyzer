# =============================================================================
# Skills ontology — comprehensive list of known technologies, tools, frameworks,
# methodologies, certifications, and domain-specific skills across 20+ categories.
# =============================================================================

SKILLS_ONTOLOGY = {
    # ==========================================================================
    # Programming Languages
    # ==========================================================================
    "programming_languages": [
        "Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "C",
        "Go", "Golang", "Rust", "Ruby", "PHP", "Swift", "Kotlin", "Scala",
        "R", "MATLAB", "Perl", "Haskell", "Clojure", "Elixir", "Erlang",
        "Dart", "Lua", "Groovy", "Objective-C", "Assembly", "COBOL",
        "Fortran", "Ada", "F#", "OCaml", "Julia", "Bash", "Shell",
        "PowerShell", "VBA", "Visual Basic", "Apex", "Solidity", "ABAP",
        "PL/SQL", "T-SQL", "SAS", "Stata", "SPSS", "Zig", "Nim",
        "Crystal", "Elm", "PureScript", "ReasonML", "ReScript",
        "VHDL", "Verilog", "SystemVerilog", "CUDA", "OpenCL",
    ],

    # ==========================================================================
    # Frontend
    # ==========================================================================
    "frontend": [
        "React", "React.js", "ReactJS", "Next.js", "NextJS",
        "Vue", "Vue.js", "VueJS", "Nuxt", "Nuxt.js", "NuxtJS",
        "Angular", "AngularJS", "Svelte", "SvelteKit",
        "Gatsby", "Remix", "Astro", "Qwik", "SolidJS", "Solid.js",
        "HTMX", "Alpine.js", "Stimulus", "Hotwire", "Turbo", "Livewire",
        "jQuery", "Redux", "Zustand", "Jotai", "XState",
        "MobX", "Recoil", "Pinia", "Vuex", "NgRx", "RxJS", "TanStack Query",
        "React Query", "SWR", "Apollo Client", "Relay",
        "HTML", "HTML5", "CSS", "CSS3", "SCSS", "SASS", "Less",
        "Tailwind CSS", "TailwindCSS", "Bootstrap", "Material UI", "MUI",
        "Chakra UI", "Ant Design", "Semantic UI", "Foundation", "Bulma",
        "Radix UI", "Headless UI", "DaisyUI", "Flowbite",
        "Styled Components", "Emotion", "CSS Modules", "PostCSS",
        "Vanilla Extract", "Panda CSS", "Linaria",
        "Webpack", "Vite", "Parcel", "esbuild", "Rollup", "Turbopack",
        "Babel", "SWC", "pnpm", "Yarn", "npm", "Nx", "Turborepo",
        "Lerna", "Rush", "Bazel", "Buck",
        "Storybook", "Chromatic", "Percy", "Figma", "Adobe XD", "Sketch",
        "Web Components", "Lit", "Stencil", "PWA", "WebAssembly", "WASM",
        "Micro Frontends", "Module Federation",
        "VitePress", "Docusaurus", "GatsbyJS",
    ],

    # ==========================================================================
    # Backend
    # ==========================================================================
    "backend": [
        "Node.js", "NodeJS", "Express", "Express.js", "Fastify", "Koa",
        "NestJS", "Nest.js", "Hono", "Elysia", "tRPC",
        "Django", "Flask", "FastAPI", "Pyramid", "Sanic", "Litestar",
        "Spring", "Spring Boot", "Hibernate", "Jakarta EE", "JAX-RS",
        "Ruby on Rails", "Rails", "Sinatra", "Laravel", "Symfony",
        "Phoenix", "ASP.NET", "ASP.NET Core", ".NET", "Blazor",
        "AdonisJS", "Feathers", "Moleculer",
        "GraphQL", "Apollo", "Apollo Server", "Prisma", "TypeORM",
        "Sequelize", "SQLAlchemy", "Django ORM", "Entity Framework",
        "Drizzle", "Knex", "Mongoose", "Dapper",
        "REST", "REST API", "RESTful", "SOAP", "gRPC", "WebSockets",
        "Socket.io", "SSE", "Server-Sent Events", "Webhooks",
        "Microservices", "Monolith", "Service-Oriented Architecture",
        "Event-Driven Architecture", "CQRS", "Event Sourcing",
        "API Gateway", "Kong", "Tyk", "Envoy",
        "RabbitMQ", "Apache Kafka", "Kafka", "Redis Pub/Sub",
        "MQTT", "ActiveMQ", "NATS", "SQS", "SNS", "EventBridge",
        "BullMQ", "Sidekiq", "Celery", "Hangfire",
        "Serverless Framework", "SST", "AWS SAM", "AWS CDK", "Pulumi",
        "Bun", "Deno",
        "Swagger", "OpenAPI", "AsyncAPI",
    ],

    # ==========================================================================
    # Databases & Storage
    # ==========================================================================
    "databases": [
        "PostgreSQL", "Postgres", "MySQL", "MariaDB", "SQLite",
        "Microsoft SQL Server", "MSSQL", "Oracle Database", "OracleDB",
        "MongoDB", "DynamoDB", "Cassandra", "CouchDB", "Couchbase",
        "Redis", "Elasticsearch", "OpenSearch", "Neo4j", "ArangoDB",
        "Firebase Firestore", "Firebase Realtime Database",
        "Supabase", "PlanetScale", "CockroachDB", "ClickHouse",
        "TimescaleDB", "InfluxDB", "Snowflake", "BigQuery", "Redshift",
        "Athena", "Presto", "Trino", "Druid", "Pinot",
        "Memcached", "Riak", "RethinkDB", "FaunaDB", "Firebird",
        "ScyllaDB", "YugabyteDB", "TiDB", "SingleStore", "Aerospike",
        "Data Warehouse", "Data Lake", "Lakehouse", "Data Mesh",
        "Delta Lake", "Apache Iceberg", "Apache Hudi",
        "Vector Database", "Pinecone", "Weaviate", "Chroma", "Chromadb",
        "Qdrant", "Milvus", "Vespa", "Elasticsearch Vector",
        "Oracle RAC", "Oracle Exadata", "Teradata", "Netezza", "Greenplum",
    ],

    # ==========================================================================
    # DevOps & Cloud
    # ==========================================================================
    "devops_cloud": [
        # AWS
        "AWS", "Amazon Web Services", "EC2", "S3", "Lambda", "RDS",
        "CloudFront", "Route 53", "Route53", "IAM", "VPC", "ELB", "EKS", "ECS",
        "Fargate", "SageMaker", "DynamoDB", "Aurora", "Redshift",
        "SQS", "SNS", "EventBridge", "Step Functions", "CloudFormation",
        "CodePipeline", "CodeBuild", "CodeDeploy", "CloudWatch", "CloudTrail",
        "API Gateway", "AWS Glue", "EMR", "Kinesis", "AWS Organizations",
        # Azure
        "Azure", "Microsoft Azure", "Azure Functions", "Azure DevOps",
        "AKS", "Azure Container Apps", "Azure SQL", "Cosmos DB", "Azure AI",
        # GCP
        "GCP", "Google Cloud Platform", "Google Cloud", "GKE",
        "Cloud Run", "Cloud Functions", "Firebase", "BigQuery",
        "Vertex AI", "Google Cloud Storage", "Pub/Sub",
        # Other cloud
        "DigitalOcean", "Heroku", "Render", "Railway", "Vercel", "Netlify",
        "Cloudflare", "Cloudflare Workers", "Akamai", "Fastly",
        "Oracle Cloud", "OCI", "IBM Cloud", "Alibaba Cloud",
        # Containers & Orchestration
        "Docker", "Docker Compose", "Docker Swarm", "Kubernetes", "K8s",
        "Helm", "Helm Charts", "OpenShift", "Rancher", "Podman",
        "Containerd", "CRI-O", "Kaniko", "Buildah",
        # IaC
        "Terraform", "OpenTofu", "Pulumi", "Ansible",
        "Puppet", "Chef", "SaltStack", "Vagrant", "Packer",
        "Crossplane", "Bicep", "Cloud Development Kit",
        # CI/CD
        "Jenkins", "GitHub Actions", "GitLab CI", "GitLab CI/CD",
        "CircleCI", "Travis CI", "Drone", "ArgoCD", "Argo Workflows",
        "Spinnaker", "TeamCity", "Bamboo", "Bitbucket Pipelines",
        "Harness", "Tekton", "Concourse", "GoCD",
        # Monitoring & Observability
        "Datadog", "New Relic", "Grafana", "Prometheus", "Loki", "Mimir",
        "Sentry", "ELK Stack", "ELK", "Logstash", "Kibana",
        "OpenTelemetry", "Jaeger", "Zipkin", "Tempo",
        "CloudWatch", "Azure Monitor", "PagerDuty", "Opsgenie", "VictorOps",
        "Dynatrace", "AppDynamics", "Sumo Logic", "Splunk",
        "Honeycomb", "Lightstep", "Chronosphere",
        # OS / Networking
        "Linux", "Unix", "Ubuntu", "Debian", "CentOS", "RHEL", "Alpine",
        "Fedora", "Arch Linux", "macOS", "Windows Server",
        "NGINX", "Apache", "Caddy", "Traefik", "HAProxy",
        "Istio", "Linkerd", "Consul", "Service Mesh",
        "Nix", "Devbox", "Dev Containers", "Dagger",
    ],

    # ==========================================================================
    # AI, Machine Learning & Data Science
    # ==========================================================================
    "ai_ml_data": [
        # ML / AI
        "Machine Learning", "Deep Learning", "Neural Networks",
        "Natural Language Processing", "NLP", "Computer Vision", "CV",
        "Reinforcement Learning", "RL", "Generative AI", "GenAI",
        "LLM", "Large Language Models", "GPT", "BERT", "Transformers",
        "Diffusion Models", "Stable Diffusion", "DALL-E", "Midjourney",
        "RAG", "Retrieval Augmented Generation", "Agents", "Agentic AI",
        "Prompt Engineering", "Fine-tuning", "RLHF", "LoRA", "QLoRA",
        # ML Frameworks
        "PyTorch", "TensorFlow", "Keras", "JAX", "Flax", "scikit-learn",
        "XGBoost", "LightGBM", "CatBoost", "MLflow", "Kubeflow",
        "Ray", "Horovod", "ONNX", "OpenVINO", "TensorRT",
        # GenAI Frameworks
        "Hugging Face", "HuggingFace", "LangChain", "LlamaIndex",
        "Semantic Kernel", "AutoGen", "CrewAI", "DSPy",
        "LangGraph", "LangSmith", "Ollama", "vLLM",
        # LLM Providers
        "OpenAI", "GPT-4", "GPT-3.5", "Anthropic", "Claude",
        "Gemini", "Google AI", "Gemma", "Mistral", "Cohere",
        "Meta AI", "Llama", "Llama 2", "Llama 3", "Grok", "xAI",
        "DeepSeek", "Qwen", "Mixtral",
        # Data Science
        "Data Science", "Data Analysis", "Data Engineering", "Data Mining",
        "Pandas", "NumPy", "SciPy", "Matplotlib", "Seaborn", "Plotly",
        "Bokeh", "Altair", "Dash", "Streamlit", "Gradio", "Shiny",
        "Tableau", "Power BI", "PowerBI", "Looker", "Metabase",
        "Apache Superset", "Preset", "Mode Analytics", "Hex",
        "Jupyter", "Google Colab", "Databricks", "Dataiku", "KNIME",
        "Alteryx", "RapidMiner", "H2O.ai", "DataRobot",
        # Big Data
        "Apache Spark", "Spark", "PySpark", "Hadoop", "Airflow", "dbt",
        "Kafka Streams", "Apache Flink", "Beam", "Dataflow",
        "ETL", "ELT", "Data Pipeline", "Data Warehouse", "Data Lake",
        "Lakehouse", "Delta Lake", "Iceberg", "Hudi",
        "Fivetran", "Stitch", "Airbyte", "Meltano", "Prefect", "Dagster",
        "A/B Testing", "Experimentation", "Hypothesis Testing",
        "Statistical Modeling", "Statistical Analysis",
        "Regression", "Classification", "Clustering", "Forecasting",
        "Time Series", "Anomaly Detection", "Causal Inference",
        "SQL", "NoSQL", "GraphQL", "SPARQL", "Data Modeling",
        "Feature Engineering", "Feature Store", "Feast", "Tecton",
        "MLOps", "Model Deployment", "Model Serving", "Model Monitoring",
        "A/B Testing", "Multi-Armed Bandit", "Contextual Bandits",
    ],

    # ==========================================================================
    # Testing & QA
    # ==========================================================================
    "testing_qa": [
        "Unit Testing", "Integration Testing", "E2E Testing",
        "API Testing", "Performance Testing", "Load Testing",
        "Stress Testing", "Chaos Engineering", "Resilience Testing",
        "Jest", "Mocha", "Chai", "Vitest", "Cypress", "Playwright",
        "Selenium", "Puppeteer", "Appium", "Detox", "Maestro",
        "Postman", "Insomnia", "JMeter", "k6", "Locust", "Artillery",
        "Gatling", "Apache Benchmark", "wrk", "Vegeta",
        "Test Automation", "TDD", "BDD", "QA", "Quality Assurance",
        "Regression Testing", "Smoke Testing", "Sanity Testing",
        "Acceptance Testing", "UAT", "Exploratory Testing",
        "Mutation Testing", "Snapshot Testing",
        "Cucumber", "SpecFlow", "Behave", "Gherkin",
        "TestRail", "Xray", "Zephyr", "qTest", "TestLink",
        "SonarQube", "SonarCloud", "Codecov", "Coveralls",
        "Pact", "Contract Testing", "Spring Cloud Contract",
        "Percy", "Applitools", "Visual Testing",
        "OWASP ZAP", "Burp Suite", "SQLMap",
    ],

    # ==========================================================================
    # Mobile Development
    # ==========================================================================
    "mobile": [
        "iOS", "Android", "React Native", "Flutter", "Xamarin",
        "SwiftUI", "UIKit", "Jetpack Compose", "Kotlin Multiplatform",
        "Mobile Development", "App Store", "Google Play",
        "TestFlight", "Crashlytics", "Firebase Analytics",
        "Mobile CI/CD", "Fastlane", "Mobile Testing",
        "Capacitor", "Ionic", "Cordova", "Expo",
        "watchOS", "tvOS", "Wear OS", "Android TV",
        "Core Data", "Room", "Realm", "SQLite",
        "Retrofit", "Alamofire", "OkHttp", "Apollo iOS",
        "Combine", "RxSwift", "RxJava", "RxKotlin",
        "FlutterFlow", "Flutter Bloc", "Provider",
    ],

    # ==========================================================================
    # Security
    # ==========================================================================
    "security": [
        "Cybersecurity", "Information Security", "OWASP",
        "Penetration Testing", "Vulnerability Assessment",
        "Security Auditing", "SOC 2", "ISO 27001", "GDPR", "HIPAA",
        "Encryption", "SSL/TLS", "PKI", "OAuth", "OpenID Connect",
        "SAML", "JWT", "Zero Trust", "Identity Management",
        "SIEM", "IDS/IPS", "WAF", "DDoS Protection",
        "Ethical Hacking", "Threat Modeling", "Incident Response",
        "DevSecOps", "SAST", "DAST", "SCA", "IAST", "RASP",
        "Snyk", "Checkmarx", "Veracode", "Fortify", "WhiteSource",
        "Aqua Security", "Sysdig", "Falco", "Twistlock",
        "Prisma Cloud", "Wiz", "Orca Security", "Lacework",
        "CrowdStrike", "SentinelOne", "Carbon Black", "Cortex XDR",
        "Cloud Security", "Container Security", "Kubernetes Security",
        "Network Security", "Endpoint Security", "Application Security",
        "SOC", "CERT", "CSIRT", "Digital Forensics",
        "NIST", "CIS", "PCI DSS", "FedRAMP", "FISMA", "CMMC",
        "Palo Alto", "Fortinet", "Cisco Security",
    ],

    # ==========================================================================
    # Blockchain & Web3
    # ==========================================================================
    "blockchain_web3": [
        "Blockchain", "Web3", "DeFi", "NFT", "Smart Contracts",
        "Ethereum", "Solana", "Polygon", "Avalanche", "BNB Chain",
        "Arbitrum", "Optimism", "Base", "zkSync", "StarkNet",
        "Solidity", "Rust", "Move", "Cairo", "Vyper",
        "Hardhat", "Truffle", "Foundry", "Brownie",
        "IPFS", "Arweave", "Filecoin", "Storj",
        "Metamask", "WalletConnect", "RainbowKit",
        "DeFi Protocols", "DEX", "Lending", "Staking", "Yield Farming",
        "Oracles", "Chainlink", "Band Protocol",
        "DAOs", "Governance Tokens", "Tokenomics",
        "The Graph", "Subgraph", "Alchemy", "Infura", "QuickNode",
    ],

    # ==========================================================================
    # Embedded Systems & Hardware
    # ==========================================================================
    "embedded_hardware": [
        "Embedded Systems", "Firmware", "Microcontroller", "Microprocessor",
        "ARM", "x86", "RISC-V", "AVR", "PIC", "MSP430",
        "Arduino", "Raspberry Pi", "ESP32", "STM32", "nRF",
        "FPGA", "ASIC", "VHDL", "Verilog", "SystemVerilog",
        "Altium", "KiCad", "Eagle", "OrCAD", "Allegro",
        "RTOS", "FreeRTOS", "Zephyr", "ThreadX", "Embedded Linux",
        "Yocto", "Buildroot", "U-Boot", "Device Tree",
        "JTAG", "SWD", "SPI", "I2C", "UART", "CAN", "Modbus",
        "IoT", "Internet of Things", "Matter", "Zigbee", "LoRa", "Bluetooth",
        "Bluetooth Low Energy", "BLE", "WiFi", "NFC", "Thread",
        "PCB Design", "PCB Layout", "Schematic Capture",
        "LabVIEW", "Simulink", "MATLAB/Simulink",
        "Sensors", "Actuators", "MEMS", "Robotics", "Motor Control",
    ],

    # ==========================================================================
    # Design & Creative
    # ==========================================================================
    "design_creative": [
        "UI Design", "UX Design", "UX Research", "User Research",
        "User Testing", "Usability Testing",
        "Wireframing", "Prototyping", "Interaction Design",
        "Visual Design", "Graphic Design", "Typography", "Color Theory",
        "Design Systems", "Component Libraries", "Responsive Design",
        "Mobile Design", "Web Design", "Product Design",
        "Figma", "Sketch", "Adobe XD", "Adobe Creative Suite",
        "Photoshop", "Illustrator", "InDesign", "After Effects",
        "Premiere Pro", "Lightroom", "Audition",
        "Framer", "Webflow", "Canva", "Penpot", "Lunacy",
        "Spline", "Rive", "Lottie", "Protopie", "Principle",
        "Accessibility", "WCAG", "a11y", "ARIA",
        "Information Architecture", "Content Strategy",
        "Motion Design", "3D Modeling", "Blender", "Cinema 4D",
        "Maya", "3ds Max", "Houdini", "ZBrush", "Substance Painter",
        "Unity", "Unreal Engine", "Godot", "Game Design",
        "CAD", "SolidWorks", "AutoCAD", "Fusion 360", "CATIA",
        "Siemens NX", "Creo", "Onshape", "Revit", "SketchUp",
        "Rhino", "Grasshopper", "Parametric Design",
        "Video Editing", "DaVinci Resolve", "Final Cut Pro",
    ],

    # ==========================================================================
    # Product & Project Management
    # ==========================================================================
    "product_project": [
        "Product Management", "Product Strategy", "Product Roadmap",
        "Product Lifecycle", "Product Discovery", "User Stories",
        "Backlog Management", "Sprint Planning", "Sprint Retrospective",
        "OKRs", "KPIs", "Metrics", "Analytics",
        "Amplitude", "Mixpanel", "Google Analytics", "GA4", "Segment",
        "Heap", "Pendo", "FullStory", "Hotjar", "Crazy Egg",
        "Aha!", "Productboard", "Miro", "Mural", "FigJam",
        "JIRA", "Confluence", "Trello", "Asana", "Linear", "Notion",
        "ClickUp", "Monday.com", "Wrike", "Smartsheet", "Basecamp",
        "Agile Methodologies", "Scrum Master", "Product Owner",
        "Agile Coaching", "Sprint Review", "Daily Standup",
        "PRD", "PRFAQ", "Working Backwards", "Opportunity Sizing",
        "Stakeholder Management", "Cross-functional Collaboration",
        "Roadmapping", "Release Management", "Feature Prioritization",
    ],

    # ==========================================================================
    # Sales, Marketing & Growth
    # ==========================================================================
    "sales_marketing": [
        # CRM
        "Salesforce", "HubSpot", "Zoho CRM", "Zendesk", "Freshworks",
        "Pipedrive", "Microsoft Dynamics", "SugarCRM",
        # Marketing
        "SEO", "SEM", "PPC", "Google Ads", "Facebook Ads", "LinkedIn Ads",
        "TikTok Ads", "Programmatic Advertising",
        "Content Marketing", "Email Marketing", "Social Media Marketing",
        "Marketing Automation", "Marketo", "Mailchimp", "Klaviyo",
        "Braze", "Iterable", "Customer.io", "ActiveCampaign",
        "Google Analytics", "GA4", "Google Tag Manager", "GTM",
        "Google Search Console", "Ahrefs", "SEMrush", "Moz",
        "Growth Hacking", "Conversion Rate Optimization", "CRO",
        "A/B Testing", "Multivariate Testing", "Optimizely", "VWO",
        "Hotjar", "Crazy Egg", "FullStory", "Heap",
        "Copywriting", "Branding", "Brand Strategy", "Brand Management",
        "PR", "Public Relations", "Media Relations",
        "Influencer Marketing", "Affiliate Marketing",
        "Lead Generation", "Demand Generation", "Account-Based Marketing",
        # Sales
        "Sales", "Enterprise Sales", "SaaS Sales", "B2B Sales",
        "Business Development", "Account Management", "Customer Success",
        "Sales Operations", "Sales Enablement", "Salesforce Admin",
        "Cold Calling", "Prospecting", "Negotiation", "Closing",
        "Pipeline Management", "Forecasting", "Territory Planning",
        "MEDDIC", "MEDDPICC", "Challenger Sale", "SPIN Selling",
        "Customer Service", "Call Center", "Help Desk",
        "Intercom", "Zendesk", "Freshdesk", "ServiceNow",
        "CSAT", "NPS", "CES", "Churn Rate", "Retention",
        "Revenue Operations", "RevOps",
    ],

    # ==========================================================================
    # Finance & Banking
    # ==========================================================================
    "finance_banking": [
        # Accounting
        "Accounting", "Bookkeeping", "QuickBooks", "Xero", "Sage",
        "Financial Reporting", "Financial Analysis", "Financial Modeling",
        "Budgeting", "Forecasting", "Financial Planning",
        "P&L", "Profit and Loss", "Balance Sheet", "Cash Flow",
        "GAAP", "IFRS", "SOX", "Sarbanes-Oxley",
        "Accounts Payable", "Accounts Receivable", "General Ledger",
        "Month-End Close", "Year-End Close", "Reconciliation",
        "Audit", "Internal Audit", "External Audit", "Tax",
        "CPA", "CFA", "CMA", "ACCA", "CA", "Chartered Accountant",
        # Finance
        "Investment Banking", "Private Equity", "VC", "Venture Capital",
        "Hedge Fund", "Asset Management", "Wealth Management",
        "M&A", "Mergers and Acquisitions", "Due Diligence",
        "Valuation", "DCF", "Comparable Company Analysis",
        "LBO", "Leveraged Buyout", "IPO",
        "Equity Research", "Credit Research", "Fixed Income",
        "Derivatives", "Options", "Futures", "Swaps", "CDS", "CDO",
        "FX", "Foreign Exchange", "Forex", "Treasury",
        "Risk Management", "Credit Risk", "Market Risk", "Operational Risk",
        "Liquidity Risk", "ALM", "Asset Liability Management",
        "VaR", "Value at Risk", "CVaR", "Expected Shortfall",
        "Stress Testing", "Scenario Analysis", "CCAR", "DFAST",
        "Basel III", "Basel IV", "Capital Adequacy",
        "PD", "Probability of Default", "LGD", "Loss Given Default",
        "EAD", "Exposure at Default", "RWA", "Risk Weighted Assets",
        "IFRS 9", "CECL", "ECL", "Expected Credit Loss",
        # Banking
        "Retail Banking", "Corporate Banking", "Commercial Banking",
        "Investment Banking", "Private Banking", "Wealth Management",
        "Trade Finance", "Supply Chain Finance", "Project Finance",
        "Mortgage", "Consumer Lending", "Small Business Lending",
        "KYC", "Know Your Customer", "AML", "Anti-Money Laundering",
        "BSA", "Bank Secrecy Act", "FATCA", "CRS",
        "Payments", "Card Payments", "ACH", "Wire Transfer", "SWIFT",
        "FinTech", "Open Banking", "PSD2", "Digital Banking",
        # Insurance
        "Insurance", "Underwriting", "Claims", "Actuarial",
        "P&C", "Property and Casualty", "Life Insurance",
        "Reinsurance", "InsurTech", "Solvency II",
        "GWP", "NWP", "Combined Ratio", "Loss Ratio",
        "CAT Modeling", "Catastrophe Modeling",
        # Tools
        "Bloomberg Terminal", "Bloomberg", "Reuters", "Eikon",
        "FactSet", "Capital IQ", "Morningstar", "Moody's Analytics",
        "SAP FICO", "Oracle Financials", "Workday Financials",
        "Anaplan", "Adaptive Insights", "Vena", "Planful",
        "Alteryx", "Tableau", "Power BI", "SAS",
        "Excel", "VBA", "Python", "R", "SQL", "MATLAB",
    ],

    # ==========================================================================
    # Healthcare & Life Sciences
    # ==========================================================================
    "healthcare_life_sciences": [
        "HIPAA", "Healthcare", "Clinical Trials", "Clinical Research",
        "FDA", "EMA", "Regulatory Affairs", "Pharmacovigilance",
        "Drug Development", "Drug Discovery", "Biotechnology",
        "Medical Devices", "In Vitro Diagnostics", "IVD",
        "EHR", "EMR", "Electronic Health Records", "HL7", "FHIR",
        "ICD-10", "CPT", "SNOMED", "LOINC", "DICOM",
        "Clinical Data Management", "CDM", "EDC", "Rave", "Medidata",
        "GCP", "Good Clinical Practice", "GLP", "GMP",
        "CRF", "eCRF", "CTMS", "eTMF", "IRT", "IWRS",
        "SAS", "R", "CDISC", "SDTM", "ADaM", "TLFs",
        "Real World Evidence", "RWE", "Real World Data", "RWD",
        "Health Economics", "HEOR", "HTA", "QALY",
        "Genomics", "Bioinformatics", "Proteomics", "Sequencing",
        "NGS", "Next Generation Sequencing", "CRISPR",
        "Healthcare IT", "Hospital Information System", "HIS",
        "RIS", "PACS", "LIS", "Laboratory Information System",
        "Telemedicine", "Telehealth", "Digital Health",
        "Medical Coding", "Medical Billing", "Revenue Cycle Management",
        "Healthcare Analytics", "Population Health",
        "Pharmaceutical", "Biopharma", "Pharmacology", "Toxicology",
        "Clinical SAS", "JMP", "GraphPad Prism",
        "CRO", "Contract Research Organization",
        "ICH Guidelines", "21 CFR Part 11", "GxP",
    ],

    # ==========================================================================
    # Legal & Compliance
    # ==========================================================================
    "legal_compliance": [
        "Legal", "Compliance", "Regulatory",
        "Contract Management", "Contract Review", "Contract Negotiation",
        "NDA", "Non-Disclosure Agreement", "MSA", "SLA",
        "GDPR", "CCPA", "CPRA", "LGPD", "PIPL",
        "Data Privacy", "Data Protection", "DPO", "DPIA",
        "AML", "KYC", "Sanctions", "OFAC", "FCPA", "UK Bribery Act",
        "SEC", "FINRA", "FCA", "ESMA", "CFTC",
        "Litigation", "Arbitration", "Mediation", "eDiscovery",
        "IP", "Intellectual Property", "Patent", "Trademark", "Copyright",
        "Corporate Law", "Employment Law", "Labor Law",
        "M&A", "Due Diligence", "Securities", "Capital Markets",
        "Tax Law", "Real Estate Law", "Environmental Law",
        "Governance", "Corporate Governance", "Board Management",
        "Risk Assessment", "Policy Development", "Policy Management",
        "Dodd-Frank", "Volcker Rule", "MiFID II", "EMIR", "Basel",
        "SOX", "COSO", "GRC", "Governance Risk and Compliance",
        "iManage", "NetDocuments", "Clio", "LexisNexis", "Westlaw",
        "Relativity", "Everlaw", "Logikcull", "Exterro",
    ],

    # ==========================================================================
    # Supply Chain & Logistics
    # ==========================================================================
    "supply_chain": [
        "Supply Chain", "Logistics", "Procurement", "Sourcing",
        "Inventory Management", "Warehouse Management", "Distribution",
        "Transportation", "Freight", "Shipping", "Last Mile",
        "Demand Planning", "Forecasting", "S&OP",
        "Lean", "Six Sigma", "Kaizen", "5S", "Value Stream Mapping",
        "ERP", "SAP", "Oracle EBS", "Microsoft Dynamics", "NetSuite",
        "SAP MM", "SAP SD", "SAP PP", "SAP WM",
        "WMS", "Manhattan Associates", "Blue Yonder", "HighJump",
        "TMS", "Oracle TMS", "MercuryGate",
        "Supplier Management", "Vendor Management", "Contract Manufacturing",
        "Strategic Sourcing", "Category Management", "Spend Analysis",
        "Purchase Orders", "RFQ", "RFP", "Negotiation",
        "Import/Export", "Customs", "Trade Compliance", "Incoterms",
        "Quality Management", "ISO 9001", "ISO 13485",
        "Cold Chain", "Reverse Logistics", "Cross-Docking",
        "Supply Chain Analytics", "Supply Chain Visibility",
        "Sustainability", "ESG", "Scope 3 Emissions",
    ],

    # ==========================================================================
    # Manufacturing & Engineering
    # ==========================================================================
    "manufacturing_engineering": [
        "Manufacturing", "Production", "Assembly", "Fabrication",
        "CNC", "Machining", "Welding", "Additive Manufacturing", "3D Printing",
        "CAD", "CAM", "CAE", "PLM", "PDM", "BOM",
        "SolidWorks", "AutoCAD", "Fusion 360", "CATIA", "Creo",
        "Siemens NX", "Inventor", "Onshape",
        "Lean Manufacturing", "Six Sigma", "Kaizen", "5S",
        "TPM", "Total Productive Maintenance", "OEE",
        "SPC", "Statistical Process Control", "Quality Control",
        "FMEA", "DFMEA", "PFMEA", "Root Cause Analysis",
        "DFM", "DFA", "Design for Manufacturing", "Design for Assembly",
        "PPAP", "APQP", "Control Plan", "MSA", "Gage R&R",
        "IATF 16949", "ISO 9001", "ISO 14001", "ISO 45001",
        "MES", "SCADA", "PLC", "HMI", "Automation",
        "Robotics", "Cobot", "Industrial Automation",
        "Process Engineering", "Chemical Engineering", "Industrial Engineering",
        "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
        "HVAC", "MEP", "Structural Engineering", "Geotechnical",
        "Project Engineering", "Construction Management",
        "Materials Science", "Metallurgy", "Polymers", "Composites",
        "Tolerance Analysis", "GD&T", "DFSS", "TRIZ",
        "Value Engineering", "Cost Reduction", "VA/VE",
        "EHS", "Environmental Health and Safety", "OSHA",
    ],

    # ==========================================================================
    # Automotive
    # ==========================================================================
    "automotive": [
        "Automotive", "OEM", "Tier 1", "Tier 2",
        "EV", "Electric Vehicle", "HEV", "PHEV", "BEV", "FCEV",
        "ICE", "Internal Combustion Engine", "Powertrain",
        "ADAS", "Autonomous Driving", "AEV", "Self-Driving",
        "LiDAR", "RADAR", "Camera Systems", "Sensor Fusion",
        "CAN", "CAN Bus", "LIN", "FlexRay", "Ethernet",
        "AUTOSAR", "ISO 26262", "Functional Safety",
        "OBD", "OBD-II", "Diagnostics", "UDS", "DoIP",
        "Vehicle Dynamics", "NVH", "Crash Safety",
        "Crash Test", "NCAP", "Euro NCAP", "IIHS",
        "Emissions", "EPA", "WLTP", "CAFE",
        "Manufacturing", "Body Shop", "Paint Shop", "Assembly Line",
        "Lean Manufacturing", "JIT", "JIS", "Heijunka",
        "Automotive SPICE", "ASPICE", "CMMI",
        "Connected Car", "V2X", "V2V", "V2I", "Telematics",
        "Infotainment", "HMI", "Instrument Cluster",
        "MATLAB", "Simulink", "Stateflow", "dSPACE", "Vector",
        "ETAS", "INCA", "CANalyzer", "CANoe", "CANape",
        "Battery", "Battery Management System", "BMS",
        "Electric Motor", "Inverter", "Power Electronics",
        "Charging", "DC Fast Charging", "Wireless Charging",
    ],

    # ==========================================================================
    # Certifications (cross-domain)
    # ==========================================================================
    "certifications": [
        # Cloud
        "AWS Certified Solutions Architect", "AWS Certified Developer",
        "AWS Certified DevOps Engineer", "AWS Certified Security",
        "AWS Certified Data Analytics", "AWS Certified Machine Learning",
        "Azure Fundamentals", "Azure Administrator", "Azure Solutions Architect",
        "Azure DevOps Engineer", "Azure Security Engineer",
        "GCP Associate Cloud Engineer", "GCP Professional Cloud Architect",
        "GCP Professional Data Engineer", "GCP Professional ML Engineer",
        # Project Management
        "PMP", "PMI-ACP", "CAPM", "CSM", "CSPO",
        "PRINCE2", "ITIL", "Six Sigma Green Belt", "Six Sigma Black Belt",
        # Security
        "CISSP", "CISM", "CISA", "CEH", "OSCP", "Security+",
        "CompTIA Security+", "CCSP", "GIAC", "GSEC",
        # Data & AI
        "TensorFlow Developer", "Azure AI Engineer",
        "Databricks Certified", "Snowflake Certified",
        "Microsoft Certified Data Analyst", "Tableau Certified",
        # Finance
        "CFA", "CPA", "CMA", "FRM", "CAIA",
        "Series 7", "Series 63", "Series 3", "CFP",
        # Agile & DevOps
        "Certified Kubernetes Administrator", "CKA",
        "Certified Kubernetes Application Developer", "CKAD",
        "HashiCorp Certified Terraform Associate",
        "Docker Certified Associate",
        # Healthcare
        "RHIA", "RHIT", "CCS", "CPC", "CHDA",
        # Engineering
        "PE", "Professional Engineer", "FE", "EIT",
        "LEED AP", "LEED Green Associate",
        # Supply Chain
        "CSCP", "CPIM", "CLTD", "SCOR-P",
        # Other
        "SAFe Agilist", "SAFe Practitioner", "SAFe Scrum Master",
        "TOGAF", "CDMP", "CBAP", "CCBA",
        "ISTQB", "ASTQB",
    ],

    # ==========================================================================
    # Soft Skills & Methodologies
    # ==========================================================================
    "soft_skills": [
        "Leadership", "Team Management", "Project Management",
        "Agile", "Scrum", "Kanban", "Waterfall", "SAFe", "Lean",
        "Communication", "Presentation", "Public Speaking",
        "Negotiation", "Conflict Resolution", "Stakeholder Management",
        "Cross-functional Collaboration", "Teamwork", "Mentoring",
        "Coaching", "Training", "Onboarding",
        "Problem Solving", "Critical Thinking", "Analytical Skills",
        "Decision Making", "Strategic Planning", "Strategic Thinking",
        "Time Management", "Prioritization", "Organization",
        "Adaptability", "Flexibility", "Resilience", "Growth Mindset",
        "Creativity", "Innovation", "Design Thinking",
        "Emotional Intelligence", "Empathy", "Active Listening",
        "Customer Focus", "Customer Success", "Client Relations",
        "Detail-Oriented", "Self-Motivated", "Initiative",
        "Accountability", "Ownership", "Results-Driven",
        "Written Communication", "Technical Writing", "Documentation",
        "Risk Management", "Change Management", "Process Improvement",
        "Vendor Management", "Budget Management", "Resource Allocation",
        "Remote Work", "Asynchronous Communication",
        "Facilitation", "Workshop Facilitation", "Brainstorming",
        "Storytelling", "Data Storytelling", "Executive Communication",
        "Influencing", "Persuasion", "Relationship Building",
        "Networking", "Business Acumen", "Commercial Awareness",
    ],

    # ==========================================================================
    # Other / General
    # ==========================================================================
    "other": [
        "Git", "GitHub", "GitLab", "Bitbucket",
        "CI/CD", "Continuous Integration", "Continuous Deployment",
        "API Design", "API Development", "API Integration",
        "SDLC", "Software Development Lifecycle",
        "Open Source", "Community Management", "Developer Relations",
        "Technical Support", "Troubleshooting", "Debugging",
        "System Design", "Architecture", "Scalability",
        "Performance Optimization", "Latency", "Throughput",
        "Code Review", "Pair Programming", "Version Control",
        "Agile", "Scrum", "Waterfall", "DevOps", "DevSecOps",
        "Linux Administration", "System Administration",
        "Networking", "DNS", "TCP/IP", "HTTP/HTTPS",
        "Microsoft Office", "Excel", "PowerPoint", "Word",
        "Google Workspace", "G Suite", "Google Docs", "Google Sheets",
        "Zoom", "Slack", "Microsoft Teams", "Discord",
        "Visio", "Lucidchart", "Draw.io", "Miro",
        "Markdown", "LaTeX",
        "Disaster Recovery", "Business Continuity",
        "On-Call", "Incident Management", "Runbooks",
        "Localization", "Internationalization", "i18n", "l10n",
        "Accessibility", "a11y", "WCAG",
        "Customer Support", "Technical Account Management",
        "Solution Architecture", "Enterprise Architecture",
        "RFP", "Proposals", "Sales Engineering",
        "Business Analysis", "Business Requirements", "BRD", "FRD",
        "Data Governance", "Data Quality", "Master Data Management",
    ],
}

FLAT_SKILLS = sorted(set(
    skill for skills in SKILLS_ONTOLOGY.values() for skill in skills
))

SKILLS_LOWER = {s.lower() for s in FLAT_SKILLS}
