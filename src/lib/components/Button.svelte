<script lang="ts">
	import { goto } from '$app/navigation';

	// Define a type for the props
	type Variant = 'primary' | 'secondary';

	// Export the props with their types
	export let variant: Variant = 'primary';
	export let classStr: string = '';
	export let href: string | null = null; // `href` can be a string or explicitly `null`

	const variantStyles = {
		primary:
			'bg-zinc-800 font-semibold text-zinc-100 hover:bg-zinc-700 active:bg-zinc-800 active:text-zinc-100/70 dark:bg-zinc-700 dark:hover:bg-zinc-600 dark:active:bg-zinc-700 dark:active:text-zinc-100/70',
		secondary:
			'bg-zinc-50 font-medium text-zinc-900 hover:bg-zinc-100 active:bg-zinc-100 active:text-zinc-900/60 dark:bg-zinc-800/50 dark:text-zinc-300 dark:hover:bg-zinc-800 dark:hover:text-zinc-50 dark:active:bg-zinc-800/50 dark:active:text-zinc-50/70'
	};

	$: combinedClasses = `${variantStyles[variant]} ${classStr} inline-flex items-center gap-2 justify-center rounded-md py-2 px-3 text-sm outline-offset-2 transition active:transition-none`;

	// A function to handle the click event, ensuring we don't call `goto` with `null`
	function handleClick(event: MouseEvent) {
		if (href) {
			// Check if `href` is not `null`
			event.preventDefault();
			goto(href); // TypeScript now understands `href` is not `null` here
		}
	}
</script>

{#if href}
	<a {href} class={combinedClasses} on:click={handleClick}>
		<slot />
	</a>
{:else}
	<button class={combinedClasses}>
		<slot />
	</button>
{/if}
