<script lang="ts">
	import { page } from '$app/state';
	import DesktopNavigation from '$lib/components/DesktopNavigation.svelte';
	import MobileNavigation from '$lib/components/MobileNavigation.svelte';
	import { i18n } from '$lib/i18n';
	import * as m from '$lib/paraglide/messages.js';
	import type { NavItem } from '$lib/types';

	let isHomePage = $derived(i18n.route(page.url.pathname) === '/');

	const navItems: NavItem[] = $state([
		{ href: '/about', text: m.about() },
		{ href: '/projects', text: m.projects() },
		{ href: '/resume', text: m.resume() },
		{ href: '/uses', text: 'Uses' }
	]);
</script>

<MobileNavigation {navItems} class="md:hidden" />
<DesktopNavigation {navItems} {isHomePage} class="hidden md:block" />
