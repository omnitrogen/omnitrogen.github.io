<!-- src/lib/components/Container.svelte -->
<script lang="ts">
	export let outer: boolean = false;
	export let inner: boolean = false;
	export let classStr: string = '';
</script>

{#if outer}
	<div class={`sm:px-8 ${classStr}`}>
		<div class="mx-auto max-w-7xl lg:px-8">
			<slot />
		</div>
	</div>
{:else if inner}
	<div class="relative px-4 sm:px-8 lg:px-12">
		<div class="mx-auto max-w-2xl lg:max-w-5xl">
			<slot />
		</div>
	</div>
{:else}
	<div class={`sm:px-8 ${classStr}`}>
		<div class="mx-auto max-w-7xl lg:px-8">
			<div class="relative px-4 sm:px-8 lg:px-12">
				<div class="mx-auto max-w-2xl lg:max-w-5xl">
					<slot />
				</div>
			</div>
		</div>
	</div>
{/if}
