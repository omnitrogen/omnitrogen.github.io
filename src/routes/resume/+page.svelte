<script lang="ts">
	import * as m from '$lib/paraglide/messages.js';
	import { languageTag } from '$lib/paraglide/runtime.js';
	import { resume } from '$content/resume';
</script>

<h1>{m.resume()}</h1>

<section>
	{#each resume.languages[languageTag()].education as e}
		<p>{e.place}</p>
		<p>{e.startDate} -> {e.endDate}</p>
	{/each}
</section>
