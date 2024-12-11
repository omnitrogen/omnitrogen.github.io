<script lang="ts">
	import Container from '$lib/components/Container.svelte';
	import BlurFade from '$lib/components/BlurFade.svelte';
	import profile from '$lib/assets/images/profile.webp';

	import * as m from '$lib/paraglide/messages.js';
</script>

<svelte:head>
	<title>Félix Defrance - Software designer, founder, and amateur astronaut</title>
	<meta
		name="description"
		content="I’m Spencer, a software designer and entrepreneur based in New York City. I’m the founder and CEO of Planetaria, where we develop technologies that empower regular people to explore space on their own terms."
	/>
</svelte:head>

<Container classStr="mt-8">
	<div class="max-w-2xl">
		<BlurFade once={true}>
			<a href="/" aria-label="Home" class="pointer-events-auto mb-4 block h-16 w-16 origin-left">
				<img
					src={profile}
					alt=""
					sizes="4rem"
					class="h-16 w-16 rounded-full bg-zinc-100 object-cover dark:bg-zinc-800"
				/>
			</a>
		</BlurFade>
		<BlurFade delay={0.12 * 1} once={true}>
			<h1
				class="mt-4 text-4xl font-bold tracking-tight text-zinc-800 sm:text-5xl dark:text-zinc-100"
			>
				{m.homeTitle()}
			</h1>
		</BlurFade>
		<BlurFade delay={0.12 * 2} once={true}>
			<p class="mt-6 text-base text-zinc-600 dark:text-zinc-400">
				I’m Spencer, a software designer and entrepreneur based in New York City. I’m the founder
				and CEO of Planetaria, where we develop technologies that empower regular people to explore
				space on their own terms.
			</p>
		</BlurFade>

		<BlurFade delay={0.12 * 3} once={true}>
			<article class="prose prose-base prose-slate lg:prose-lg dark:prose-invert">
				<h4>hello world!</h4>

				<p>I am Félix, a software engineer from France.</p>

				<p>
					I like to create softwares that are sustainable, accessible, useful, fast and lightweight.
				</p>

				<p>
					I currently work at the <b>French National Museum of Natural History</b> (MNHN) where I am
					in charge of redesigning a <i>citizen science</i> mobile app that allow french citizens to
					participate in the french biodiversity inventory.
				</p>

				<p>My ideal tech stacks would be:</p>

				<ul>
					<li>
						for the web
						<ul>
							<li>
								frontend with
								<a href="https://kit.svelte.dev/" target="_blank" rel="noopener noreferrer"
									>sveltekit</a
								>
							</li>
							<li>
								backend either
								<a href="https://github.com/tokio-rs/axum" target="_blank" rel="noopener noreferrer"
									>axum</a
								>
								(rust) with
								<a
									href="https://github.com/launchbadge/sqlx"
									target="_blank"
									rel="noopener noreferrer">sqlx</a
								>
								and a custom
								<a href="https://www.postgresql.org/" target="_blank" rel="noopener noreferrer"
									>postgres</a
								>
								db, or a solution like
								<a href="https://supabase.com/" target="_blank" rel="noopener noreferrer"
									>supabase</a
								>
							</li>
						</ul>
					</li>
					<li>
						for native mobile app
						<ul>
							<li>
								<a href="https://flutter.dev/" target="_blank" rel="noopener noreferrer">flutter</a>
								with
								<a href="https://riverpod.dev/" target="_blank" rel="noopener noreferrer"
									>riverpod</a
								>
								and
								<a href="https://isar.dev/" target="_blank" rel="noopener noreferrer">isar</a>
							</li>
						</ul>
					</li>
				</ul>

				<p>
					Besides programming, I enjoy spending time outdoors running all kind of trails, cycling
					long distances, skiing up and down mountains and growing our family vegetable garden.
				</p>

				<p>
					I am quite terrified by the climate crisis, I care about social justice and I am
					fascinated by sustainable mobility.
				</p>

				<span>If you wish to contact me, you can reach me there: </span>

				<ul>
					<li>felixgif at gmail dot com</li>
				</ul>

				<span><i>Fun</i> facts:</span>
				<ul>
					<li>I really love rice</li>
					<li>someday, I want to live in a tiny house deep in the french Alps</li>
					<li>
						I am an
						<a
							href="https://www.16personalities.com/infp-personality"
							target="_blank"
							rel="noopener noreferrer">INFP</a
						>
					</li>
				</ul>

				<blockquote>
					"All that is gold does not glitter,<br />
					Not all those who wander are lost;<br />
					The old that is strong does not wither,<br />
					Deep roots are not reached by the frost."

					<footer>
						<cite>- J.R.R. Tolkien, The Fellowship of the Ring</cite>
					</footer>
				</blockquote>
			</article>
		</BlurFade>
	</div>
</Container>
