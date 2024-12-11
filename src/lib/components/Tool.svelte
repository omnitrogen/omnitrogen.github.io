<script lang="ts">
	import Card from './Card.svelte';

	export let href = '';
	export let title = '';
</script>

<Card as="li">
	<Card Title titleAs="h3" {href}>
		{title}
	</Card>
	<Card Description><slot /></Card>
</Card>
