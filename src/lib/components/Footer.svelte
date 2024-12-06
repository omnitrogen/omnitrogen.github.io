<script lang="ts">
	import * as m from '$lib/paraglide/messages.js';

	import CodeXml from 'lucide-svelte/icons/code-xml';
</script>

<footer>
	<section>
		<small>
			<span><CodeXml size={24} /> {m.footerWith()} ❤️ {m.footerBy()}</span>
		</small>
	</section>
</footer>

<style>
	footer {
		text-align: center;
		margin-bottom: 2rem;
	}
</style>
