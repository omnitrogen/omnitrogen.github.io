<script>
	import '@picocss/pico';
	import './styles.css';
	import Header from '../components/Header.svelte';
	import Footer from '../components/Footer.svelte';
</script>

<div class="app">
	<main class="container">
		<Header />

		<body>
			<slot />
		</body>

		<Footer />
	</main>
</div>
