<script lang="ts">
	import { i18n } from '$lib/i18n';
	import { page } from '$app/stores';
	import { languageTag } from '$lib/paraglide/runtime.js';

	import * as m from '$lib/paraglide/messages.js';

	import GraduationCap from 'lucide-svelte/icons/graduation-cap';
	import Shapes from 'lucide-svelte/icons/shapes';
</script>

<header class="container-fluid">
	<nav>
		<ul>
			<li>
				<a href="/"><strong>felixonwheels</strong></a>
			</li>
		</ul>
		<ul>
			<li>
				<a href="/resume"><strong><GraduationCap size={32} /> {m.resume()}</strong></a>
			</li>
			<li>
				<a href="/projects"><strong><Shapes size={32} /> {m.projects()}</strong></a>
			</li>
			<li>
				<a
					role="button"
					class="outline"
					aria-current={languageTag() ? 'page' : undefined}
					href={i18n.route($page.url.pathname)}
					hreflang={languageTag() === 'fr' ? 'en' : 'fr'}
				>
					{languageTag() === 'fr' ? '🇬🇧' : '🇫🇷'}
				</a>
			</li>
		</ul>
	</nav>
</header>

<style>
	header {
		/* margin: 0 1rem 2rem; */
		margin-bottom: 1rem;
	}

	nav {
		display: flex;
		flex-direction: row;
	}

	@media (width <= 576px) {
		header {
			margin: 0 0 2rem;
		}

		nav {
			flex-direction: column;
		}

		ul:nth-child(1) {
			justify-content: center;
		}

		ul:nth-child(2) {
			justify-content: space-around;
		}
	}
</style>
