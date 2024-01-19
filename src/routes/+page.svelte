<svelte:head>
	<title>félix defrance</title>
	<meta name="description" content="homepage" />
</svelte:head>

<section>
	<section class="centered">
		<img src="/images/profile.webp" alt="félix defrance profile" />
	</section>

	<h4>hello world!</h4>

	<p>I am Félix, a software engineer from France.</p>

	<hr />

	<p>I like to create softwares that are sustainable, accessible, useful, fast and lightweight.</p>

	<p>
		I currently work at the <b>French National Museum of Natural History</b> (MNHN) where I am in charge of redesigning
		a <i>citizen science</i> mobile app that allow french citizens to participate in the french biodiversity inventory.
	</p>

	<hr />

	<p>My ideal tech stacks would be:</p>

	<ul>
		<li>
			for the web
			<ul>
				<li>
					frontend with
					<code><a href="https://kit.svelte.dev/" target="_blank" rel="noopener noreferrer">sveltekit</a></code>
				</li>
				<li>
					backend either
					<code><a href="https://github.com/tokio-rs/axum" target="_blank" rel="noopener noreferrer">axum</a></code>
					(rust) with
					<code><a href="https://github.com/launchbadge/sqlx" target="_blank" rel="noopener noreferrer">sqlx</a></code>
					and a custom
					<code><a href="https://www.postgresql.org/" target="_blank" rel="noopener noreferrer">postgres</a></code>
					db, or a solution like
					<code><a href="https://supabase.com/" target="_blank" rel="noopener noreferrer">supabase</a></code>
				</li>
			</ul>
		</li>
		<li>
			for native mobile app
			<ul>
				<li>
					<code><a href="https://flutter.dev/" target="_blank" rel="noopener noreferrer">flutter</a></code>
					with
					<code><a href="https://riverpod.dev/" target="_blank" rel="noopener noreferrer">riverpod</a></code>
					and
					<code><a href="https://isar.dev/" target="_blank" rel="noopener noreferrer">isar</a></code>
				</li>
			</ul>
		</li>
	</ul>

	<hr />

	<p>
		Besides programming, I enjoy spending time outdoors running all kind of trails, cycling long distances, skiing up
		and down mountains and growing our family vegetable garden.
	</p>

	<p>
		I am quite terrified by the climate crisis, I care about social justice and I am fascinated by sustainable mobility.
	</p>

	<hr />

	<span>If you wish to contact me, you can reach me there: </span>

	<ul>
		<li>felixgif at gmail dot com</li>
	</ul>

	<hr />

	<span><i>Fun</i> facts:</span>
	<ul>
		<li>I really love rice</li>
		<li>someday, I want to live in a tiny house deep in the french Alps</li>
		<li>
			I am an
			<a href="https://www.16personalities.com/infp-personality" target="_blank" rel="noopener noreferrer">INFP</a>
		</li>
	</ul>

	<hr />

	<blockquote>
		All that is gold does not glitter,<br />
		Not all those who wander are lost;<br />
		The old that is strong does not wither,<br />
		Deep roots are not reached by the frost.
		<footer>
			<cite>- J.R.R. Tolkien, The Fellowship of the Ring</cite>
		</footer>
	</blockquote>
</section>

<style>
	img {
		border-radius: 4rem;
		width: 10vh;
		height: 10vh;
		object-fit: cover;
	}

	.centered {
		text-align: center;
		margin-bottom: 1rem;
	}
</style>
