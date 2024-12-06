<script lang="ts">
	import { i18n } from '$lib/i18n';
	import { ParaglideJS } from '@inlang/paraglide-sveltekit';
	import '@picocss/pico/css/pico.jade.min.css';
	import Footer from '$lib/components/Footer.svelte';
	import Header from '$lib/components/Header.svelte';
	import '../style.css';

	let { children } = $props();
</script>

<ParaglideJS {i18n}>
	<main>
		<Header />

		<div class="container">
			{@render children()}
		</div>

		<Footer />
	</main>
</ParaglideJS>
