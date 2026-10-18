<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Arun M | Full Stack Developer & AI/ML Engineer</title>
<style>
  :root{
    --bg:#0D0D1A; --bg2:#1a0533; --bg3:#0d1b4b;
    --purple:#a855f7; --violet:#7c3aed; --sky:#38bdf8; --green:#22c55e;
    --text:#e2e8f0; --muted:#94a3b8; --card:rgba(26,5,51,.55); --border:rgba(168,85,247,.35);
  }
  *{box-sizing:border-box;margin:0;padding:0}
  html{scroll-behavior:smooth}
  body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;line-height:1.6;overflow-x:hidden}
  a{color:inherit;text-decoration:none}
  .wrap{max-width:1000px;margin:0 auto;padding:0 20px}

  /* ===== HERO ===== */
  .hero{position:relative;text-align:center;padding:90px 20px 110px;overflow:hidden;
    background:linear-gradient(135deg,var(--bg) 0%,var(--bg2) 35%,var(--bg3) 70%,var(--bg) 100%)}
  .orb{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(168,85,247,.45),transparent 70%);animation:pulse 6s ease-in-out infinite}
  .orb.a{width:340px;height:340px;left:8%;top:-40px}
  .orb.b{width:380px;height:380px;right:6%;top:40px;animation-delay:-3s}
  @keyframes pulse{0%,100%{transform:scale(.85);opacity:.7}50%{transform:scale(1.15);opacity:1}}
  .star{position:absolute;width:3px;height:3px;background:#fff;border-radius:50%;animation:twinkle 2.5s ease-in-out infinite}
  @keyframes twinkle{0%,100%{opacity:.1}50%{opacity:1}}
  .float{position:absolute;font-family:'Courier New',monospace;font-size:24px;color:var(--purple);opacity:.5;animation:bob 4s ease-in-out infinite}
  @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-16px)}}
  .name{position:relative;font-size:clamp(52px,11vw,104px);font-weight:800;letter-spacing:2px;
    background:linear-gradient(90deg,var(--purple),var(--sky),var(--purple));background-size:200% auto;
    -webkit-background-clip:text;background-clip:text;color:transparent;animation:shine 5s linear infinite,fadein 1.2s ease both}
  @keyframes shine{to{background-position:200% center}}
  @keyframes fadein{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
  .role{position:relative;font-size:clamp(16px,3vw,24px);letter-spacing:3px;color:var(--text);animation:fadein 1.6s .4s ease both}
  .bar{position:relative;height:3px;width:0;margin:14px auto 0;background:var(--purple);border-radius:2px;animation:grow 1.5s .8s ease forwards}
  @keyframes grow{to{width:240px}}
  .typing{position:relative;margin-top:26px;font-family:'JetBrains Mono','Courier New',monospace;font-weight:700;font-size:clamp(14px,2.6vw,20px);color:var(--purple);min-height:30px}
  .typing::after{content:'|';margin-left:2px;animation:blink 1s steps(1) infinite}
  @keyframes blink{50%{opacity:0}}
  .wave{position:absolute;left:0;bottom:-1px;width:200%;height:70px;animation:slide 9s linear infinite}
  .wave.w2{animation-duration:6s;opacity:.6;bottom:-8px}
  @keyframes slide{to{transform:translateX(-50%)}}

  /* ===== BUTTONS / BADGES ===== */
  .links{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin:34px 0 10px}
  .btn{padding:10px 20px;border-radius:8px;font-weight:700;font-size:14px;color:#fff;transition:.25s;box-shadow:0 0 0 rgba(168,85,247,0)}
  .btn:hover{transform:translateY(-4px);box-shadow:0 8px 24px rgba(168,85,247,.45)}
  .li{background:#0077B5}.gh{background:#181717;border:1px solid #333}.pf{background:#00C7B7}.em{background:#D14836}
  .pill{display:inline-block;padding:3px 11px;margin:3px 2px;border-radius:999px;font-size:12px;font-weight:600;background:var(--bg2);border:1px solid var(--border);color:#e9d5ff}
  .pill.sky{background:#0c2a4a;border-color:var(--sky);color:#bae6fd}
  .pill.green{background:#14532d;border-color:var(--green);color:#bbf7d0}
  .center{text-align:center}

  /* ===== DIVIDER ===== */
  .divider{position:relative;height:2px;margin:46px 0;background:linear-gradient(90deg,transparent,var(--purple),var(--sky),transparent)}
  .divider::after{content:'';position:absolute;top:-4px;width:10px;height:10px;border-radius:50%;background:var(--sky);box-shadow:0 0 14px var(--sky);animation:run 4s ease-in-out infinite alternate}
  @keyframes run{from{left:0}to{left:calc(100% - 10px)}}

  h2{font-size:28px;margin-bottom:22px;background:linear-gradient(90deg,var(--purple),var(--sky));-webkit-background-clip:text;background-clip:text;color:transparent;display:inline-block}
  section{padding:0 0}
  .reveal{opacity:0;transform:translateY(30px);transition:.8s}
  .reveal.show{opacity:1;transform:none}

  /* ===== ABOUT ===== */
  .about{display:grid;grid-template-columns:1.4fr 1fr;gap:28px;align-items:center}
  .about p{margin-bottom:12px}
  code{background:var(--bg2);border:1px solid var(--border);padding:2px 8px;border-radius:6px;color:var(--sky);font-size:14px}
  .avatar{width:100%;max-width:280px;margin:auto;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;font-size:96px;font-weight:800;
    background:conic-gradient(from 0deg,var(--purple),var(--sky),var(--violet),var(--purple));animation:spin 8s linear infinite;position:relative}
  .avatar span{position:absolute;inset:6px;border-radius:50%;background:var(--bg);display:grid;place-items:center;animation:spin 8s linear infinite reverse}
  @keyframes spin{to{transform:rotate(360deg)}}

  /* ===== MARQUEE ===== */
  .marquee{overflow:hidden;border-radius:12px;background:#0b0b18;padding:14px 0;
    -webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
  .track{display:flex;gap:12px;width:max-content;animation:marq 28s linear infinite}
  .marquee:hover .track{animation-play-state:paused}
  @keyframes marq{to{transform:translateX(-50%)}}
  .chip{padding:8px 22px;border-radius:999px;font-weight:700;font-size:14px;white-space:nowrap;border:1px solid var(--purple);background:var(--bg2);color:#e9d5ff}
  .chip.s{border-color:var(--sky);background:#0c2a4a;color:#bae6fd}

  /* ===== PROJECTS ===== */
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
  .card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:24px;backdrop-filter:blur(6px);transition:.3s;position:relative;overflow:hidden}
  .card::before{content:'';position:absolute;inset:-2px;background:conic-gradient(from 0deg,transparent,var(--purple),transparent 30%);opacity:0;transition:.4s;z-index:0;animation:spin 5s linear infinite}
  .card:hover::before{opacity:.25}
  .card>*{position:relative;z-index:1}
  .card:hover{transform:translateY(-6px);border-color:var(--purple);box-shadow:0 14px 40px rgba(124,58,237,.3)}
  .card.full{grid-column:1/-1}
  .card h3{font-size:20px;margin-bottom:6px}
  .card h3 a:hover{color:var(--sky)}
  .card .desc{color:var(--muted);font-style:italic;margin-bottom:10px}
  .card ul{list-style:none;margin-top:10px}
  .card li{padding:3px 0}
  .card h4{margin:14px 0 4px;color:var(--sky);font-size:15px}
  .tag{float:right;font-size:12px;padding:3px 10px;border-radius:999px;background:var(--violet);color:#fff}
  .cols{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}

  /* ===== TIMELINE ===== */
  .timeline{position:relative;padding-left:30px;border-left:2px solid var(--border)}
  .job{position:relative;margin-bottom:28px;background:var(--card);border:1px solid var(--border);border-radius:14px;padding:18px 22px;transition:.3s}
  .job:hover{transform:translateX(8px);border-color:var(--sky)}
  .job::before{content:'';position:absolute;left:-39px;top:24px;width:14px;height:14px;border-radius:50%;background:var(--c,var(--purple));box-shadow:0 0 0 0 var(--c,var(--purple));animation:ping 2s infinite}
  @keyframes ping{70%{box-shadow:0 0 0 12px transparent}100%{box-shadow:0 0 0 0 transparent}}
  .job h3{font-size:18px}.job .date{color:var(--muted);font-size:13px;margin-bottom:6px}

  /* ===== TABLE ===== */
  table{width:100%;border-collapse:collapse;background:var(--card);border-radius:14px;overflow:hidden;border:1px solid var(--border)}
  th,td{padding:12px 16px;text-align:left;border-bottom:1px solid rgba(168,85,247,.15)}
  th{background:var(--bg2);color:var(--sky)}
  tr:hover td{background:rgba(124,58,237,.12)}

  /* ===== STATS ===== */
  .stats{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;align-items:center}
  .stats img{max-width:100%;border-radius:12px}
  .snake{width:100%;border-radius:14px;background:var(--card);border:1px solid var(--border);padding:12px}

  footer{text-align:center;padding:60px 20px 80px;color:var(--muted)}
  footer blockquote{margin:20px 0;font-style:italic}

  @media(max-width:760px){
    .about,.grid,.cols{grid-template-columns:1fr}
    .float{display:none}
  }
  @media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.reveal{opacity:1;transform:none}}
</style>
</head>
<body>

<!-- ================= HERO ================= -->
<header class="hero" id="hero">
  <div class="orb a"></div><div class="orb b"></div>
  <span class="float" style="left:8%;top:35%">&lt;/&gt;</span>
  <span class="float" style="right:9%;top:28%;animation-delay:-1s;color:var(--sky)">{ }</span>
  <span class="float" style="right:20%;bottom:20%;animation-delay:-2s;color:var(--sky)">AI</span>
  <span class="float" style="left:16%;bottom:22%;animation-delay:-1.5s;color:var(--sky)">01</span>

  <h1 class="name">Arun M</h1>
  <p class="role">Full Stack Developer &nbsp;|&nbsp; AI / ML Engineer</p>
  <div class="bar"></div>
  <p class="typing" id="typing"></p>

  <div class="links">
    <a class="btn li" href="https://linkedin.com/in/arunvijay-5a2845317" target="_blank" rel="noopener">LinkedIn</a>
    <a class="btn gh" href="https://github.com/Arun597134" target="_blank" rel="noopener">GitHub</a>
    <a class="btn pf" href="https://arunmportfolioin.netlify.app" target="_blank" rel="noopener">Portfolio</a>
    <a class="btn em" href="mailto:arun.m.dev06@gmail.com">Email</a>
  </div>

  <svg class="wave" viewBox="0 0 2000 70" preserveAspectRatio="none"><path fill="#7c3aed" fill-opacity=".45" d="M0 35 C250 0 500 70 750 35 S1250 0 1500 35 S1750 70 2000 35 L2000 70 L0 70Z"/></svg>
  <svg class="wave w2" viewBox="0 0 2000 70" preserveAspectRatio="none"><path fill="#0D0D1A" d="M0 45 C300 15 500 70 1000 45 S1700 15 2000 45 L2000 70 L0 70Z"/></svg>
</header>

<main class="wrap">

  <!-- ================= ABOUT ================= -->
  <section class="reveal" style="margin-top:50px">
    <h2>🧠 About Me</h2>
    <div class="about">
      <div>
        <p>👋 Hey! I'm <b>Arun M</b> — a passionate <b>Full Stack Developer</b> and <b>AI/ML Engineer</b> from Chennai, India 🇮🇳</p>
        <p>🎓 Pursuing <b>B.Tech in AI &amp; Data Science</b> at St. Joseph's Institute of Technology &nbsp;<code>CGPA: 8.21 / 10</code></p>
        <p>🚀 Currently building a <b>MERN Learning Management System</b> with role-based access &amp; AI integration</p>
        <p>🤖 I love crafting intelligent systems — from NLP pipelines to real-time proctoring engines</p>
        <p>💡 Fun fact: <i>I make machines learn so I don't have to!</i></p>
        <div style="margin-top:12px">
          <span class="pill">👤 Arun M</span><span class="pill">💼 Full Stack | AI/ML</span><span class="pill">📍 Chennai, India</span>
          <span class="pill">🎓 CGPA 8.21 / 10</span><span class="pill">🔨 Building MERN LMS</span><span class="pill green">✅ Open To Opportunities</span>
        </div>
      </div>
      <div class="avatar"><span>AM</span></div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ================= TECH ================= -->
  <section class="reveal">
    <h2>🛠️ Tech Arsenal</h2>
    <div class="marquee"><div class="track" id="track"></div></div>
    <div class="center" style="margin-top:18px">
      <span class="pill sky">Redux Toolkit</span><span class="pill sky">JWT</span><span class="pill sky">Pandas</span><span class="pill sky">NumPy</span>
      <span class="pill sky">Cloudinary</span><span class="pill sky">Oracle Cloud</span><span class="pill sky">Render</span><span class="pill sky">TensorFlow.js</span>
      <span class="pill sky">PostgreSQL</span><span class="pill sky">Airflow</span><span class="pill sky">Kafka</span>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ================= PROJECTS ================= -->
  <section class="reveal">
    <h2>🚀 Featured Projects</h2>
    <div class="grid">

      <div class="card">
        <h3>🤖 <a href="https://github.com/Arun597134/Hirewise-AI" target="_blank" rel="noopener">HireWise AI — Mock Interviewer</a></h3>
        <p class="desc">AI-powered interview simulator with NLP resume parsing</p>
        <span class="pill">Python</span><span class="pill">NLP</span><span class="pill">scikit-learn</span><span class="pill">Tkinter</span>
        <ul><li>📄 NLP resume parsing &amp; keyword extraction</li><li>❓ 20+ tailored questions per session</li><li>📈 <b>40% boost</b> in question relevance</li><li>🔄 End-to-end automated interview flow</li></ul>
      </div>

      <div class="card">
        <h3>🎓 <a href="https://github.com/arunvijay/assessment-platform" target="_blank" rel="noopener">AI Assessment Platform</a></h3>
        <p class="desc">Full-stack exam platform with AI proctoring</p>
        <span class="pill sky">React</span><span class="pill sky">Node.js</span><span class="pill sky">MongoDB</span><span class="pill">TF.js</span>
        <ul><li>📷 Webcam proctoring via TensorFlow.js</li><li>🚫 Tab-switch tracking &amp; fullscreen lock</li><li>📊 Real-time integrity scores</li><li>🏆 Leaderboard &amp; analytics dashboard</li></ul>
      </div>

      <div class="card full">
        <span class="tag">In Development 🔨</span>
        <h3>📚 MERN Learning Management System</h3>
        <p class="desc">Full-stack LMS with role-based access and AI-proxied ML services</p>
        <span class="pill sky">React</span><span class="pill sky">Redux</span><span class="pill sky">Node.js</span><span class="pill sky">MongoDB</span><span class="pill">JWT</span><span class="pill sky">Tailwind</span>
        <ul><li>🔐 JWT auth + bcrypt + refresh token sessions</li><li>👥 Roles: <b>Student</b>, <b>Instructor</b>, <b>Admin</b></li><li>📹 Per-session video progress tracking</li><li>🔍 Search, domain filtering &amp; paginated listings</li><li>📝 Timestamped notes &amp; session bookmarks</li><li>🤖 AI/ML services proxied through backend</li></ul>
      </div>

      <div class="card full">
        <h3>🏛️ <a href="https://github.com/Arun597134/" target="_blank" rel="noopener">CivicFlow — AI Civic Complaint Platform</a></h3>
        <p class="desc">AI-powered municipal complaint management platform for Tamil Nadu citizens &amp; administrators</p>
        <span class="pill sky">React/Vite</span><span class="pill">Flask</span><span class="pill">Python</span><span class="pill">SQLite</span><span class="pill">JWT</span><span class="pill">scikit-learn</span>
        <div class="cols">
          <div><h4>🤖 AI &amp; ML Core</h4><ul><li>👁️ AI Vision parses complaint images → auto-routes to dept</li><li>⏱️ ML delay prediction from category + history</li><li>💰 Anti-corruption cost estimate capped at ₹500</li></ul></div>
          <div><h4>🗺️ Hyper-Local Ops</h4><ul><li>📍 All <b>38 TN districts</b> down to town/village</li><li>🚗 Ola-style live officer assignment dashboard</li><li>📡 Citizens track officer &amp; status live</li></ul></div>
          <div><h4>🌍 Citizen Empowerment</h4><ul><li>🌐 Tamil localization via translation widget</li><li>✅ Full CRUD on own complaints</li><li>🔐 Separate JWT portals for Citizens &amp; Admins</li></ul></div>
        </div>
      </div>

      <div class="card full">
        <span class="tag">Aug 2026</span>
        <h3>🏗️ Enterprise Data Ingestion &amp; Validation Framework</h3>
        <p class="desc">Hybrid batch + streaming ingestion framework with SQL-pushdown validation and automated monitoring</p>
        <span class="pill">Python</span><span class="pill sky">PostgreSQL</span><span class="pill sky">Airflow</span><span class="pill">Kafka</span><span class="pill">SQL Pushdown</span>
        <ul><li>🔀 Hybrid <b>batch + streaming</b> ingestion using Airflow &amp; Kafka</li><li>✅ <b>SQL-pushdown validation</b> — checks run inside PostgreSQL, not in Python memory</li><li>📡 Automated monitoring for pipeline health &amp; data quality</li><li>⚡ <b>36× reduction in memory usage</b></li></ul>
      </div>

    </div>
  </section>

  <div class="divider"></div>

  <!-- ================= EXPERIENCE ================= -->
  <section class="reveal">
    <h2>💼 Experience</h2>
    <div class="timeline">
      <div class="job" style="--c:#7c3aed">
        <h3>🟣 Prodigy Infotech — Software Dev Intern</h3><div class="date">Jul – Aug 2025</div>
        <span class="pill">✔ Scalable UI Modules</span><span class="pill">✔ 10+ Bug Fixes</span><span class="pill">✔ CI/CD Deployments</span><span class="pill">✔ Git Version Control</span>
      </div>
      <div class="job" style="--c:#0ea5e9">
        <h3>🔵 Codtech IT Solutions — Web Dev Intern</h3><div class="date">2024 – 2025</div>
        <span class="pill sky">✔ 3+ Responsive Pages</span><span class="pill sky">✔ RESTful API Integration</span><span class="pill sky">✔ Git Branching Workflows</span>
      </div>
      <div class="job" style="--c:#f97316">
        <h3>🟠 Codsoft IT Solutions — Java Programming Intern</h3><div class="date">Jan – Feb 2025</div>
        <span class="pill">✔ 5+ OOP &amp; DSA Programs</span><span class="pill">✔ Reusable Module Refactoring</span><span class="pill">✔ Code Review &amp; Optimization</span>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ================= CERTS ================= -->
  <section class="reveal">
    <h2>🏆 Certifications</h2>
    <table>
      <tr><th>🎖️ Certificate</th><th>🏫 Issuer</th><th>🛠️ Topics</th></tr>
      <tr><td>Front End Web Developer</td><td>Infosys</td><td>HTML · CSS · JS · Responsive Design</td></tr>
      <tr><td>Basics of MongoDB</td><td>MongoDB</td><td>NoSQL · Collections · Queries</td></tr>
      <tr><td>OCI AI Foundations</td><td>Oracle</td><td>Cloud Infrastructure · AI Services</td></tr>
      <tr><td>Intro to Large Language Models</td><td>Google Cloud</td><td>LLM Concepts · Prompt Engineering</td></tr>
      <tr><td>Intro to Generative AI</td><td>Google Cloud</td><td>GenAI · Foundation Models</td></tr>
    </table>
  </section>

  <div class="divider"></div>

  <!-- ================= STATS ================= -->
  <section class="reveal">
    <h2>📊 GitHub Stats</h2>
    <div class="stats">
      <img height="180" alt="GitHub stats" src="https://github-readme-stats.vercel.app/api?username=Arun597134&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true&hide_border=true" />
      <img height="180" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Arun597134&layout=compact&langs_count=8&theme=tokyonight&hide_border=true" />
      <img alt="Streak" src="https://streak-stats.demolab.com?user=Arun597134&theme=tokyonight&hide_border=true" />
    </div>
  </section>

  <div class="divider"></div>

  <!-- ================= CONTRIBUTIONS ================= -->
  <section class="reveal">
    <h2>📈 Contribution Graph</h2>
    <div class="snake center">
      <img style="max-width:100%" alt="Contribution calendar" src="https://ghchart.rshah.org/7c3aed/Arun597134" />
    </div>
    <div class="snake center" style="margin-top:16px">
      <img style="max-width:100%" alt="Activity graph" src="https://github-readme-activity-graph.vercel.app/graph?username=Arun597134&bg_color=0D0D1A&color=A855F7&line=7C3AED&point=38BDF8&area_color=7C3AED&area=true&hide_border=true&custom_title=Contribution%20Activity" />
    </div>
  </section>

</main>

<footer>
  <h3 style="color:var(--text)">Let's connect and build something impactful!</h3>
  <div class="links">
    <a class="btn li" href="https://linkedin.com/in/arunvijay-5a2845317" target="_blank" rel="noopener">Connect on LinkedIn</a>
    <a class="btn pf" href="https://arunmportfolioin.netlify.app" target="_blank" rel="noopener">View Portfolio</a>
    <a class="btn em" href="mailto:arun.m.dev06@gmail.com">Send Email</a>
  </div>
  <blockquote>"It works on my machine" — Arun M, probably 🤷‍♂️</blockquote>
</footer>

<script>
  // Typing effect
  (function(){
    var lines=["🚀 Building Scalable Web Applications","🤖 Engineering Intelligent AI/ML Systems","⚡ React | Node.js | MongoDB | Python","🔮 Turning Data into Smart Solutions"];
    var el=document.getElementById('typing'),l=0,c=0,del=false;
    function tick(){
      var t=lines[l];
      el.textContent=t.slice(0,c);
      if(!del&&c<t.length){c++;setTimeout(tick,70)}
      else if(!del){del=true;setTimeout(tick,1400)}
      else if(c>0){c--;setTimeout(tick,35)}
      else{del=false;l=(l+1)%lines.length;setTimeout(tick,300)}
    }
    tick();
  })();

  // Stars
  (function(){
    var hero=document.getElementById('hero');
    for(var i=0;i<40;i++){
      var s=document.createElement('span');s.className='star';
      s.style.left=Math.random()*100+'%';s.style.top=Math.random()*100+'%';
      s.style.animationDelay=(Math.random()*3)+'s';s.style.animationDuration=(2+Math.random()*2)+'s';
      hero.appendChild(s);
    }
  })();

  // Skills marquee (duplicated for seamless loop)
  (function(){
    var skills=["Python","JavaScript","Java","React","Node.js","Express","MongoDB","TensorFlow","scikit-learn","Redux","Tailwind","Flask","PostgreSQL","Airflow","Kafka","Git"];
    var html='';
    for(var r=0;r<2;r++){skills.forEach(function(s,i){html+='<span class="chip'+(i%2?' s':'')+'">'+s+'</span>'})}
    document.getElementById('track').innerHTML=html;
  })();

  // Scroll reveal
  (function(){
    var els=document.querySelectorAll('.reveal');
    if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('show')});return}
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('show');io.unobserve(x.target)}})},{threshold:.12});
    els.forEach(function(e){io.observe(e)});
  })();
</script>
</body>
</html>
