<script lang="ts">
	import Card from './Card.svelte';

	export let Section: boolean = false;
	export let Tools: boolean = false;
	export let Appearance: boolean = false;
	export let SpeakingSection: boolean = false;

	export let href = '';
	export let title = '';
	export let event = '';
	export let description = '';
	export let cta = '';
</script>

{#if Section || SpeakingSection}
	<section class="md:border-l md:border-zinc-100 md:pl-6 md:dark:border-zinc-700/40">
		<div class="grid max-w-3xl grid-cols-1 items-baseline gap-y-8 md:grid-cols-4">
			<h2 class="text-sm font-semibold text-zinc-800 dark:text-zinc-100">
				{title}
			</h2>
			<div class="md:col-span-3">
				{#if SpeakingSection}
					<div class="space-y-16"><slot /></div>
				{:else if Tools}
					<ul role="list" class="space-y-16">
						<slot />
					</ul>
				{:else}
					<slot />
				{/if}
			</div>
		</div>
	</section>
{:else if Appearance}
	<Card cardAs="article">
		<Card Title titleAs="h3" {href}>{title}</Card>
		<Card Eyebrow decorate>{event}</Card>
		<Card Description>{description}</Card>
		<Card Cta>{cta}</Card>
	</Card>
{/if}
