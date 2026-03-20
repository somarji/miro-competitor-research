import marimo

__generated_with = "0.17.6"
app = marimo.App(width="full", app_title="Competitor Research — Miro 2026")


@app.cell
def __():
    import marimo as mo
    import re
    from pathlib import Path
    from datetime import date
    return Path, date, mo, re


@app.cell
def __(mo):
    # Inject Miro design tokens into the page
    _styles = mo.Html("""<style>
    body, html {
        background: #FAFAFA !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    </style>""")
    return (_styles,)


@app.cell
def __(Path):
    SNAPSHOTS_DIR = Path(__file__).parent / "snapshots"
    BASE_DIR = Path(__file__).parent
    TRACK_FIELD = {
        "All":         None,
        "Voice":       "voice_quality",
        "Proactivity": "proactivity",
        "Identity":    "unique_identity",
    }

    # Miro brand palette
    SCORE_PALETTE = {
        "high":           ("#D4F5E2", "#0D7F3F"),
        "med":            ("#FFF7CC", "#8B6914"),
        "medium":         ("#FFF7CC", "#8B6914"),
        "low":            ("#FFE5E8", "#C0293B"),
        "needs research": ("#F0F0EF", "#6B6B6B"),
    }
    SCORE_LABELS = {
        "high": "High", "med": "Med", "medium": "Med",
        "low": "Low", "needs research": "Needs Research",
    }
    REL_BORDER = {
        "platform threat":        "#FF6683",  # Miro red
        "direct competitor":      "#4262FF",  # Miro blue
        "inspiration":            "#6EDB8C",  # Miro green
        "adjacent":               "#A0A0B0",  # neutral
        "adjacent / encroaching": "#ff9d48",  # Miro orange
    }
    return BASE_DIR, REL_BORDER, SCORE_LABELS, SCORE_PALETTE, SNAPSHOTS_DIR, TRACK_FIELD


@app.cell
def __(re):
    def parse_frontmatter(text):
        meta, body = {}, text
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                for line in parts[1].strip().splitlines():
                    if ":" in line:
                        k, _, v = line.partition(":")
                        meta[k.strip().lower().replace(" ", "_")] = v.strip()
                body = parts[2].strip()
        return meta, body

    def extract_section(body, heading):
        pat = re.compile(
            rf"(?m)^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
            re.DOTALL | re.MULTILINE,
        )
        m = pat.search(body)
        if not m:
            return "", body
        content = m.group(1).strip()
        remainder = (body[: m.start()] + body[m.end() :]).strip()
        return content, remainder

    def parse_changelog(raw):
        entries = []
        for line in raw.splitlines():
            s = line.strip().lstrip("-").strip()
            if not s:
                continue
            m = re.match(r"\*{0,2}(\d{4}-\d{2}-\d{2})\*{0,2}[:\s-]+(.*)", s)
            entries.append((m.group(1), m.group(2).strip()) if m else ("", s))
        return entries

    return extract_section, parse_changelog, parse_frontmatter


@app.cell
def __():
    # Snapshot content embedded for WASM export — filesystem unavailable in browser
    EMBEDDED_SNAPSHOTS = {
        "elevenlabs.md": """---
name: ElevenLabs
tier: Market Leader
relationship: Inspiration
voice_quality: High
proactivity: Low
unique_identity: High
last_updated: 2026-03-10
---

## Overview
ElevenLabs is not a canvas competitor — it's the category-defining benchmark for what AI voice identity should feel and sound like. At an **$11B valuation** ($500M Series D, February 2026), Eleven v3 delivers emotionally expressive, character-specific voice synthesis. If Miro ever adds a voice layer to Sidekicks, ElevenLabs is the likely infrastructure and the design standard to match.

## Recent Changes
- **2026-02-14**: $500M Series D closed at $11B valuation, led by Sequoia
- **2026-02-01**: Eleven v3 model launched — expressive, character-specific voice with emotional weight
- **2026-01-20**: Matthew McConaughey licensing deal announced — first major celebrity synthetic voice persona
- **2025-12-05**: Voice Agent API v2 released — lower latency, better turn-taking for conversational agents
- **2025-11-01**: Voice Cloning Pro launched with legal persona protection framework

## What Miro Can Learn
The McConaughey licensing deal signals that AI voice identity is becoming a legal and brand asset. When Miro designs a "Miro Facilitator" voice persona, it will need a legal and IP strategy, not just a product one. ElevenLabs' expressiveness benchmark: a voice that carries personality, emotion, and presence — not just information.""",

        "figjam.md": """---
name: FigJam
tier: Market Leader
relationship: Direct Competitor
voice_quality: Med
proactivity: Med
unique_identity: Med
last_updated: 2026-02-20
---

## Overview
FigJam is the closest canvas-to-canvas competitor. It benefits from deep integration with the Figma design ecosystem, making it a gravitational default for product and design teams. FigJam AI (Jambot + generative templates) shows users want AI embedded *in the canvas moment*, not in a sidebar — the right instinct, but execution is currently reactive rather than proactive.

## Recent Changes
- **2026-02-20**: Jambot updated with GPT-5.2; faster responses and longer context window on boards
- **2026-01-18**: AI template generation from natural language prompts now available on all paid plans
- **2026-01-05**: Sticky clustering and summarization shipped as first-class features
- **2025-11-12**: FigJam audio feature expanded — spatial voice comments now persist on boards
- **2025-10-01**: Image generation integrated directly on canvas via Figma AI

## What Miro Can Learn
FigJam's integration with the Figma file graph (designs, prototypes, dev handoff) in a single surface is a strong pull for design-led teams. Miro's answer is breadth across *all* team types — not just design. The lesson: own a specific team motion as deeply as FigJam owns design sprints.""",

        "google_gemini.md": """---
name: Google Gemini
tier: Market Leader
relationship: Platform Threat
voice_quality: Med
proactivity: High
unique_identity: Low
last_updated: 2026-03-17
---

## Overview
Google's Gemini has evolved from a chatbot into a proactive personal intelligence layer across the entire Workspace suite. **Workspace Studio** lets enterprise teams build and share AI agents natively in Docs, Sheets, Slides, and Meet — without leaving Google. The Jamboard-to-Miro migration audience is now Gemini's active re-acquisition target.

## Recent Changes
- **2026-03-17**: Gemini 3.1 integrated into Search and Chrome — surfaces proactively while users browse
- **2026-02-28**: Goal Scheduled Actions enter beta — Gemini adapts its next action based on the output of the previous run
- **2026-02-10**: Workspace Studio goes GA — enterprise agent builder native in Google Workspace
- **2026-01-15**: Gemini Personal Intelligence launched — pulls proactive context from Gmail, Photos, YouTube, Drive
- **2025-12-01**: Gemini Agent ships — multi-step task execution with approval gates before high-stakes actions

## What Miro Can Learn
Goal Scheduled Actions (where the AI reads its prior output before acting again) is the right architecture for Miro's recurring workshop AI — retros, standups, sprint reviews should get *incrementally smarter* each week, not just re-run the same clustering job.""",

        "hume_ai.md": """---
name: Hume AI
tier: Emerging Startup
relationship: Inspiration
voice_quality: High
proactivity: Med
unique_identity: High
last_updated: 2026-02-15
---

## Overview
Hume AI's **Empathic Voice Interface (EVI)** reads and responds to emotional subtext in real time — not just the words, but the tone, pace, and sentiment beneath them. In blind head-to-head tests against ElevenLabs, Hume leads on nuanced emotional delivery. For Miro, this is the vision of what a workshop facilitator AI could become: one that senses when a team is stuck, frustrated, or misaligned.

## Recent Changes
- **2026-02-15**: EVI 3.0 released — sub-200ms emotional response latency, 30% improvement in sentiment accuracy
- **2026-01-20**: Enterprise API launched — voice emotion signals now available as structured data for downstream apps
- **2026-01-05**: Hume raises Series B; expands team and research into multi-speaker emotion tracking
- **2025-11-10**: Group sentiment analysis added — can track emotional state of multiple speakers simultaneously
- **2025-09-01**: Research paper published: emotional voice signals outperform text-only AI in conflict de-escalation

## What Miro Can Learn
Multi-speaker sentiment tracking is directly applicable to Miro's Engage product. An AI facilitator that surfaces "the team seems stuck — here's a reframe technique" based on voice and text tone would be a genuinely novel capability. EVI's emotional fingerprinting approach is the architecture to study.""",

        "microsoft_copilot.md": """---
name: Microsoft Copilot
tier: Market Leader
relationship: Platform Threat
voice_quality: Low
proactivity: High
unique_identity: Low
last_updated: 2026-03-18
---

## Overview
Wave 3 (March 9, 2026) marks Microsoft's most aggressive agentic push yet. **Copilot Cowork** — powered by Anthropic Claude — handles long-running multi-step work autonomously, while a **leaked Copilot Canvas** spec describes an AI whiteboard with image generation and live collaboration. Combined with MURAL's existing Copilot integration, Microsoft is assembling every component needed to displace Miro in enterprise.

## Recent Changes
- **2026-03-09**: Wave 3 announced — Copilot Cowork enters research preview, Agent 365 launch set for May 1
- **2026-03-01**: Copilot Canvas leaked — AI-powered whiteboard with image generation and AI streaming
- **2026-02-15**: Agent Recommendations ship — Copilot proactively suggests relevant agents mid-conversation
- **2026-02-01**: Multi-agent coordination enabled — agents can call other agents as tools
- **2026-01-10**: Microsoft unifies Copilot under new leadership to drive "agentic AI future"

## What Miro Can Learn
The multi-agent handoff model (one agent's completion triggers another) is the architecture Miro Sidekicks need. A Research Sidekick → Synthesis Sidekick → Presentation Sidekick pipeline — executing without a human re-prompting between steps — is the enterprise proactivity playbook.""",

        "mural.md": """---
name: MURAL
tier: Emerging Startup
relationship: Direct Competitor
voice_quality: Low
proactivity: High
unique_identity: Med
last_updated: 2026-03-05
---

## Overview
MURAL is Miro's closest historical competitor and has differentiated sharply in 2026 by becoming the **only visual collaboration tool** in the initial Microsoft 365 Copilot third-party integration set. Its LUMA System facilitation methodology embedded into AI is a meaningful identity play — MURAL positions itself as a branded way of working, not just a canvas tool.

## Recent Changes
- **2026-03-05**: MURAL AI sentiment analysis now surfaces team mood scores during retrospectives
- **2026-02-01**: Microsoft 365 Copilot integration deepened — Copilot can now generate MURAL boards from Teams meetings
- **2026-01-10**: LUMA System facilitation patterns embedded into AI workflow templates
- **2025-12-15**: MURAL AI clustering and mind map generation reach feature parity with Miro
- **2025-11-01**: Enterprise SSO via Entra ID tightened — MURAL is now the Microsoft-endorsed canvas

## What Miro Can Learn
MURAL's bet on methodology-as-identity (LUMA System) is the right instinct. "It's not just a canvas, it's a way of working" is a stronger brand position than feature lists. Miro should ask: does it have an equivalent methodological identity that its AI can embody?""",

        "notion_ai.md": """---
name: Notion AI
tier: Emerging Startup
relationship: Adjacent / Encroaching
voice_quality: Low
proactivity: High
unique_identity: Low
last_updated: 2026-03-01
---

## Overview
Notion 3.3 (February 24, 2026) launched **Custom Agents** — proactive, autonomous AI teammates that live in the workspace, run on triggers and schedules, and act 24/7 without prompting. Over 21,000 Custom Agents were created in early access. Notion is steadily eating into Miro's async synthesis and documentation territory.

## Recent Changes
- **2026-02-24**: Notion 3.3 ships Custom Agents — schedule, event, and Slack triggers; 21,000+ created in early testing
- **2026-01-20**: Notion 3.2 brings agents to mobile with voice-to-text prompting
- **2026-01-20**: Auto-model selection added — GPT-5.2, Claude Opus 4.5, Gemini 3 all available
- **2025-09-18**: Notion 3.0 launches with first Agents feature — reactive AI teammates
- **2025-08-01**: Notion AI reaches 4M paying users

## What Miro Can Learn
Custom Agents' trigger architecture is the clearest model for what Miro's proactive AI should do. The key insight: agents have a *narrow, explicit job description* — they don't do everything, they do one thing reliably. Miro Sidekicks with tight scope (one trigger, one output) will be more trusted than broad ambient intelligence.""",

        "openai.md": """---
name: OpenAI
tier: Market Leader
relationship: Platform Threat
voice_quality: High
proactivity: High
unique_identity: Med
last_updated: 2026-03-18
---

## Overview
OpenAI's ChatGPT now combines a voice-first interface with the **Operator** agentic layer — browsing, clicking, and completing tasks without prompting. GPT-5.4 hit a 75% success rate on the OSWorld benchmark, nearing human-level software navigation. The ChatGPT canvas mode is the closest Big Tech equivalent to Miro's spatial thinking surface.

## Recent Changes
- **2026-03-09**: Operator agent merged into ChatGPT as a unified agentic interface — no separate product needed
- **2026-02-18**: GPT-5.4 released; achieves 75% on OSWorld (vs. 72.4% human baseline)
- **2026-01-22**: Advanced Voice Mode v2 ships with lower latency and expanded emotional range
- **2026-01-05**: ChatGPT canvas mode exits beta; spatial brainstorm + edit surface now generally available
- **2025-12-10**: OpenAI joins Agentic AI Foundation (Linux Foundation) alongside Google, Microsoft, Anthropic

## What Miro Can Learn
Operator's task delegation UX — where users hand off a goal and check back at milestones — is the right mental model for Miro Sidekicks. The user stays in control without re-prompting at every step.""",

        "polyai.md": """---
name: PolyAI
tier: Emerging Startup
relationship: Inspiration
voice_quality: Med
proactivity: High
unique_identity: Med
last_updated: 2026-01-15
---

## Overview
PolyAI ($750M valuation, $86M Series D, December 2025) is the enterprise playbook for **AI identity consistency at scale**. With 2,000+ live deployments across 45 languages, its voice agents maintain brand-consistent AI identity across every interaction — a Forrester study documented 391% ROI over three years. For Miro, PolyAI is less a competitor and more a model for how to govern a deployed AI persona globally.

## Recent Changes
- **2026-01-15**: PolyAI expands into EMEA with new London engineering hub; 45-language support now GA
- **2025-12-20**: $86M Series D closed at $750M valuation; 100+ enterprise customers confirmed
- **2025-12-01**: Identity governance framework published — white paper on maintaining brand-consistent AI voice at scale
- **2025-11-10**: Outbound proactive call initiation feature GA — agents now initiate based on CRM triggers
- **2025-10-01**: Multi-brand agent support — single deployment can maintain distinct personas per brand/product line

## What Miro Can Learn
PolyAI's multi-brand persona model (one deployment, distinct personalities per context) is directly applicable to Miro's enterprise scale challenge. As Sidekicks roll out globally, how does "Miro Facilitator" sound and behave the same whether you're in Tokyo, Berlin, or São Paulo? PolyAI's identity governance framework is the operational playbook to study.""",

        "sesame.md": """---
name: Sesame
tier: Emerging Startup
relationship: Inspiration
voice_quality: High
proactivity: Med
unique_identity: High
last_updated: 2026-02-01
---

## Overview
Sesame (backed by a16z, Spark Capital, Matrix) is building the clearest current demonstration of **AI Identity done right**: a persistent, character-consistent voice companion that breathes naturally, pauses, shifts emotional register, and adapts to the user over time. Users describe it as the closest thing to "Jarvis in real life." For Miro, Sesame answers the question: what would it feel like to have a Miro Facilitator that teams actually develop a relationship with?

## Recent Changes
- **2026-02-01**: Sesame v2 ships — improved long-term memory, persona consistency across sessions
- **2026-01-10**: Voice naturalness benchmark published — Sesame scores highest on "felt human" in third-party evaluations
- **2025-12-15**: Series B closed (amount undisclosed) led by a16z; expansion into enterprise companion use cases
- **2025-11-01**: Proactive check-ins added — Sesame initiates conversation based on user activity gaps and calendar context
- **2025-09-20**: Emotional memory launched — Sesame remembers how you felt during past conversations and references it contextually

## What Miro Can Learn
Sesame's proactive check-ins (triggered by activity gaps and calendar context) are the right model for Miro Sidekick proactivity: low-friction, contextually appropriate, not intrusive. The deeper lesson is that AI identity is *earned over time* through consistency — a Miro Facilitator persona needs to behave the same way in every session to become trusted.""",
    }
    return (EMBEDDED_SNAPSHOTS,)


@app.cell
def __(EMBEDDED_SNAPSHOTS, SNAPSHOTS_DIR, extract_section, parse_changelog, parse_frontmatter):
    def _load(name, raw):
        _meta, _body = parse_frontmatter(raw)
        _cl_raw, _body = extract_section(_body, "Recent Changes")
        if not _cl_raw:
            _cl_raw, _body = extract_section(_body, "Change Log")
        _learn_raw, _body = extract_section(_body, "What Miro Can Learn")
        _overview_raw, _ = extract_section(_body, "Overview")
        return {
            "name":            _meta.get("name", name.replace("_", " ").title()),
            "tier":            _meta.get("tier", ""),
            "relationship":    _meta.get("relationship", ""),
            "voice_quality":   _meta.get("voice_quality", ""),
            "proactivity":     _meta.get("proactivity", ""),
            "unique_identity": _meta.get("unique_identity", ""),
            "last_updated":    _meta.get("last_updated", ""),
            "overview":        _overview_raw,
            "changelog":       parse_changelog(_cl_raw)[:4],
            "learn":           _learn_raw,
        }

    # Try local filesystem first; fall back to embedded data in WASM
    snapshots = []
    if SNAPSHOTS_DIR.exists():
        for _path in sorted(SNAPSHOTS_DIR.glob("*.md")):
            snapshots.append(_load(_path.stem, _path.read_text(encoding="utf-8")))
    else:
        for _fname, _raw in sorted(EMBEDDED_SNAPSHOTS.items()):
            snapshots.append(_load(_fname.replace(".md", ""), _raw))
    return (snapshots,)


@app.cell
def __(mo):
    track_select = mo.ui.radio(
        options=["All", "Voice", "Proactivity", "Identity"],
        value="All",
        label="Research Track",
    )
    refresh_btn = mo.ui.button(label="🔄 Refresh Data", kind="neutral")
    return refresh_btn, track_select


@app.cell
def __(mo, refresh_btn, track_select):
    sidebar = mo.sidebar(
        [
            mo.md("## 🧭 Research Track"),
            track_select,
            mo.md("---"),
            refresh_btn,
        ]
    )
    return (sidebar,)


@app.cell
def __(BASE_DIR, mo, refresh_btn):
    _monitor_out = mo.md("")
    if refresh_btn.value:
        try:
            import subprocess as _sp
            _res = _sp.run(
                ["python3", str(BASE_DIR / "monitor.py")],
                capture_output=True, text=True, cwd=str(BASE_DIR),
            )
            _text = (_res.stdout or _res.stderr or "monitor.py: no output.").strip()
            _monitor_out = mo.callout(
                mo.md(f"**monitor.py output:**\n```\n{_text}\n```"),
                kind="info",
            )
        except Exception:
            _monitor_out = mo.callout(
                mo.md("Refresh is available locally only — run `python3 monitor.py` in your terminal."),
                kind="warn",
            )
    refresh_output = _monitor_out
    return (refresh_output,)


@app.cell
def __(mo, refresh_output, snapshots):
    _tiers = sorted({s["tier"] for s in snapshots if s["tier"]})
    _rels  = sorted({s["relationship"] for s in snapshots if s["relationship"]})

    search      = mo.ui.text(placeholder="Search by name or keyword…", full_width=True)
    tier_filter = mo.ui.multiselect(_tiers, label="Tier")
    rel_filter  = mo.ui.multiselect(_rels,  label="Relationship")

    _header = mo.Html("""
    <div style="background:#050038;border-radius:12px;padding:24px 28px;
                display:flex;align-items:center;gap:16px;">
      <div style="background:#FFD02F;width:40px;height:40px;border-radius:8px;
                  display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-size:20px;font-weight:900;color:#050038;line-height:1;">M</span>
      </div>
      <div>
        <div style="font-size:20px;font-weight:800;color:#FFFFFF;
                    font-family:'Inter',sans-serif;letter-spacing:-.02em;">
          Competitor Research
        </div>
        <div style="font-size:13px;color:#8888AA;margin-top:2px;">
          AI Landscape &nbsp;·&nbsp; Voice, Proactivity, Identity &nbsp;·&nbsp; 2026
        </div>
      </div>
    </div>""")

    controls = mo.vstack([
        _header,
        mo.hstack([search, tier_filter, rel_filter], gap="1rem", align="end"),
        refresh_output,
    ], gap="1rem")
    return controls, rel_filter, search, tier_filter


@app.cell
def __(controls):
    controls


@app.cell
def __(TRACK_FIELD, rel_filter, search, snapshots, tier_filter, track_select):
    _q    = search.value.lower().strip()
    _tiers = set(tier_filter.value)
    _rels  = set(rel_filter.value)
    _track_field = TRACK_FIELD[track_select.value]

    filtered = [
        s for s in snapshots
        if (not _q or _q in s["name"].lower() or _q in s["overview"].lower())
        and (not _tiers or s["tier"] in _tiers)
        and (not _rels  or s["relationship"] in _rels)
        and (_track_field is None
             or s.get(_track_field, "").lower() in ("high", "med", "medium"))
    ]
    return (filtered,)


@app.cell
def __(REL_BORDER, SCORE_LABELS, SCORE_PALETTE, filtered, mo):
    def _score_badge(label, value):
        key = (value or "").lower().strip()
        bg, fg = SCORE_PALETTE.get(key, ("#F0F0EF", "#6B6B6B"))
        display = SCORE_LABELS.get(key, value or "—")
        return (
            f'<div style="flex:1;text-align:center;padding:10px 6px;border-radius:8px;background:{bg};">'
            f'<div style="font-size:10px;color:{fg};font-weight:700;text-transform:uppercase;'
            f'letter-spacing:.08em;margin-bottom:3px;font-family:Inter,sans-serif;">{label}</div>'
            f'<div style="font-size:18px;font-weight:800;color:{fg};font-family:Inter,sans-serif;">{display}</div>'
            f'</div>'
        )

    def _pill(text, bg, fg):
        return (
            f'<span style="font-size:11px;font-weight:600;color:{fg};background:{bg};'
            f'padding:3px 10px;border-radius:32px;margin-right:4px;'
            f'font-family:Inter,sans-serif;">{text}</span>'
        )

    def _changelog_rows(entries):
        if not entries:
            return '<p style="color:#A0A0B0;font-size:13px;font-family:Inter,sans-serif;">No recent changes logged.</p>'
        rows = ""
        for d, desc in entries:
            if d:
                import html as _html
                rows += (
                    f'<div style="display:flex;gap:10px;padding:6px 0;'
                    f'border-bottom:1px solid #F0F0EF;">'
                    f'<code style="font-size:11px;color:#4262FF;white-space:nowrap;'
                    f'flex-shrink:0;font-weight:600;">{_html.escape(d)}</code>'
                    f'<span style="font-size:13px;color:#333350;line-height:1.5;'
                    f'font-family:Inter,sans-serif;">{_html.escape(desc)}</span>'
                    f'</div>'
                )
            else:
                import html as _html
                rows += (
                    f'<div style="padding:4px 0;font-size:13px;color:#333350;'
                    f'font-family:Inter,sans-serif;">· {_html.escape(desc)}</div>'
                )
        return rows

    def _render_card(s):
        border_color = REL_BORDER.get(s["relationship"].lower(), "#E0E0E0")

        tier_bg = "#EEF2FF" if "leader" in s["tier"].lower() else "#EDFBF3"
        tier_fg = "#4262FF" if "leader" in s["tier"].lower() else "#0D7F3F"
        tier_pill = _pill(s["tier"], tier_bg, tier_fg) if s["tier"] else ""
        rel_pill  = _pill(s["relationship"], "#F5F5F5", "#6B6B6B") if s["relationship"] else ""

        scores = (
            '<div style="display:flex;gap:8px;margin:14px 0;">'
            + _score_badge("🎙 Voice",       s["voice_quality"])
            + _score_badge("⚡ Proactivity",  s["proactivity"])
            + _score_badge("🎭 AI Identity",  s["unique_identity"])
            + '</div>'
        )

        changelog_html = (
            '<div style="margin-top:16px;">'
            '<div style="font-size:11px;font-weight:700;color:#A0A0B0;text-transform:uppercase;'
            'letter-spacing:.08em;margin-bottom:8px;font-family:Inter,sans-serif;">Recent Changes</div>'
            + _changelog_rows(s["changelog"])
            + '</div>'
        )

        learn_html = ""
        if s["learn"]:
            import html as _html
            _learn = _html.escape(s["learn"])
            learn_html = (
                '<div style="margin-top:16px;padding:12px 14px;background:#FFF7CC;'
                'border-radius:8px;border-left:3px solid #FFD02F;">'
                '<div style="font-size:11px;font-weight:700;color:#8B6914;'
                'text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px;'
                'font-family:Inter,sans-serif;">💡 Miro Can Learn</div>'
                f'<div style="font-size:13px;color:#050038;line-height:1.6;'
                f'font-family:Inter,sans-serif;white-space:pre-wrap;">{_learn}</div>'
                '</div>'
            )

        overview_html = ""
        if s["overview"]:
            import re as _re, html as _html
            plain = _re.sub(r'\*{1,2}([^*]+)\*{1,2}', r'\1', s["overview"])
            plain = _re.sub(r'#{1,6}\s*', '', plain)
            plain = _html.escape(plain)
            overview_html = (
                f'<div style="font-size:13px;color:#6B6B6B;line-height:1.6;margin:10px 0 0;'
                f'padding-bottom:12px;border-bottom:1px solid #F0F0EF;'
                f'font-family:Inter,sans-serif;">'
                f'{plain}</div>'
            )

        footer = (
            f'<div style="margin-top:14px;font-size:11px;color:#A0A0B0;'
            f'font-family:Inter,sans-serif;">Updated {s["last_updated"]}</div>'
        ) if s["last_updated"] else ""

        return (
            f'<div style="background:#FFFFFF;border-radius:8px;padding:20px;'
            f'box-shadow:0 2px 8px rgba(5,0,56,.07);border:1px solid #E8E8F0;'
            f'border-top:4px solid {border_color};height:100%;box-sizing:border-box;">'
            f'<div style="margin-bottom:6px;">'
            f'<span style="font-size:17px;font-weight:800;color:#050038;'
            f'font-family:Inter,sans-serif;letter-spacing:-.01em;">{s["name"]}</span>'
            f'</div>'
            f'<div style="margin-bottom:2px;">{tier_pill}{rel_pill}</div>'
            + overview_html
            + scores
            + changelog_html
            + learn_html
            + footer
            + '</div>'
        )

    # Build grid: 3 cards per row
    _rows = []
    for _i in range(0, len(filtered), 3):
        _chunk = filtered[_i:_i + 3]
        # pad to 3 so grid stays even
        while len(_chunk) < 3:
            _chunk.append(None)
        _cells = []
        for _s in _chunk:
            if _s:
                _cells.append(mo.Html(_render_card(_s)))
            else:
                _cells.append(mo.Html('<div></div>'))
        _rows.append(mo.hstack(_cells, gap="1.2rem", widths="equal"))

    if not filtered:
        cards = mo.callout(
            mo.md("**No competitors match your filters.** Try clearing the search or adjusting the Research Track."),
            kind="warn",
        )
    else:
        _n = len(filtered)
        _count = mo.Html(
            f'<div style="font-size:13px;font-weight:600;color:#6B6B6B;'
            f'font-family:Inter,sans-serif;padding:4px 0;">'
            f'{_n} competitor{"s" if _n != 1 else ""} shown</div>'
        )
        cards = mo.vstack([_count] + _rows, gap="1rem")

    return (cards,)


@app.cell
def __(cards):
    cards


if __name__ == "__main__":
    app.run()
