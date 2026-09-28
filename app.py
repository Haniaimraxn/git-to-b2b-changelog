import os
import sys
from github import Github, GithubException
from google import genai

# Rich UI modules for terminal formatting
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt

# Initialize Rich Console
console = Console()


def fetch_recent_commits(repo_name: str, max_commits: int = 10) -> str:
    """Fetches the latest commit messages from a public GitHub repository."""
    github_token = os.environ.get("GITHUB_TOKEN")
    
    # Initialize GitHub client (authenticated if token exists, unauthenticated otherwise)
    g = Github(github_token) if github_token else Github()

    try:
        repo = g.get_repo(repo_name)
        commits = repo.get_commits()[:max_commits]
        
        commit_logs = []
        for commit in commits:
            # Extract first line of the commit message
            raw_msg = commit.commit.message.split("\n")[0].strip()
            author = commit.commit.author.name if commit.commit.author else "Unknown Contributor"
            commit_logs.append(f"- {raw_msg} (by {author})")
            
        if not commit_logs:
            raise ValueError("No commits found in the specified repository.")

        return "\n".join(commit_logs)
    except GithubException as e:
        if e.status == 403 and not github_token:
            raise RuntimeError(
                "GitHub API rate limit exceeded for unauthenticated requests. "
                "Please set your GITHUB_TOKEN environment variable."
            ) from e
        raise RuntimeError(f"GitHub API Error [{e.status}]: {e.data.get('message', str(e))}") from e
    except Exception as e:
        raise RuntimeError(f"Failed to fetch commits from '{repo_name}': {e}") from e


def generate_b2b_changelog(commit_logs: str) -> str:
    """Sends commit logs to Gemini 2.5 Flash to generate a B2B product announcement."""
    # Retrieve API key strictly from environment variables
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing Gemini API Key. Please export GEMINI_API_KEY or GOOGLE_API_KEY in your environment."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an expert B2B Product Marketer and Technical Writer.

Translate the following raw technical git commit logs into a compelling, high-converting B2B product changelog.

Target Audience: Executive Stakeholders, CTOs, and Business Clients.

Structure the response into these exact sections:
1. 🚀 Major Highlights: Summarize the biggest user-facing value or impact in 1-2 punchy sentences.
2. ✨ Key Features & Improvements: Group technical changes into business benefits (ROI, performance, security, UX).
3. 🛠️ Technical Details: A concise bulleted list of underlying technical updates.
4. 💡 Call to Action: A short closing line encouraging clients to try the updates or read docs.

Raw Commit Logs:
{commit_logs}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def main():
    console.clear()

    # ── Modern Tech Header Banner ──────────────────────────────────
    header = r"""
  ██████╗ ██╗████████╗    ████████╗██████╗     ██████╗ ██████╗ ██████╗ 
 ██╔════╝ ██║╚══██╔══╝    ╚══██╔══╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗
 ██║  ███╗██║   ██║          ██║   ██║  ██║    ██████╔╝██████╔╝██████╔╝
 ██║   ██║██║   ██║          ██║   ██║  ██║    ██╔══██╗██╔══██╗██╔═══╝ 
 ╚██████╔╝██║   ██║          ██║   ██████╔╝    ██████╔╝██████╔╝██║     
  ╚═════╝ ╚═╝   ╚═╝          ╚═╝   ╚═════╝     ╚═════╝ ╚═════╝ ╚═╝     
    """
    console.print(
        Panel(
            header,
            style="bold cyan",
            title="[bold white]B2B AI Changelog Engine[/bold white]",
            subtitle="Powered by Gemini 2.5 Flash",
        )
    )

    # ── User Input Prompt ──────────────────────────────────────────
    repo_input = Prompt.ask("\n[bold yellow]Enter Target Repository[/bold yellow]", default="pallets/flask")

    commit_logs = None
    changelog_md = None

    # ── Single-Task Dynamic Progress Bar ───────────────────────────
    with Progress(
        SpinnerColumn("dots", style="cyan"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:

        # Step 1: Fetch Commits
        task_id = progress.add_task(
            description=f"Fetching recent commits from [bold green]{repo_input}[/bold green]...",
            total=None,
        )
        try:
            commit_logs = fetch_recent_commits(repo_input, max_commits=10)
        except Exception as e:
            progress.stop()
            console.print(f"\n[bold red]❌ GitHub Error:[/bold red] {e}\n")
            sys.exit(1)

        # Step 2: AI Processing
        progress.update(task_id, description="Translating commits to Executive B2B Format using Gemini...")
        try:
            changelog_md = generate_b2b_changelog(commit_logs)
        except Exception as e:
            progress.stop()
            console.print(f"\n[bold red]❌ AI Generation Error:[/bold red] {e}\n")
            sys.exit(1)

    # ── Formatted Output Rendering ─────────────────────────────────
    console.print("\n")
    changelog_panel = Panel(
        Markdown(changelog_md),
        title=f"[bold green]✨ Executive Product Announcement — {repo_input}[/bold green]",
        border_style="cyan",
        padding=(1, 2),
    )

    console.print(changelog_panel)
    console.print("\n[bold dim green]✔ Changelog generated successfully![/bold dim green]\n")


if __name__ == "__main__":
    main()