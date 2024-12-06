<script lang="ts">
	import { i18n } from '$lib/i18n';
	import { page } from '$app/stores';
	import { languageTag } from '$lib/paraglide/runtime.js';

	import * as m from '$lib/paraglide/messages.js';

	import GraduationCap from 'lucide-svelte/icons/graduation-cap';
	import Shapes from 'lucide-svelte/icons/shapes';
</script>

<header>
	<nav>
		<ul>
			<li>
				<a role="button" class="contrast" href="/"><strong>felixonwheels</strong></a>
			</li>
		</ul>
		<ul>
			<li>
				<a role="button" href="/resume"><strong><GraduationCap size={32} /> {m.resume()}</strong></a
				>
			</li>
			<li>
				<a role="button" href="/projects"><strong><Shapes size={32} /> {m.projects()}</strong></a>
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
		margin: 1rem 0;
	}

	nav {
		display: flex;
		flex-direction: row;
	}

	@media (width <= 576px) {
		nav {
			flex-direction: column;
			align-items: center;
			justify-content: center;
		}
	}
</style>
