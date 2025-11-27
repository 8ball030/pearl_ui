<!-- We add in the background and center everything -->
<script lang="ts">
	import Counter from '../components/counter.svelte';
	import Table from '../components/parameterTable.svelte';
</script>

<main
	class="flex min-h-screen flex-col items-center justify-center gap-6 bg-primary p-4 text-primary-foreground"
>
	<h1>Welcome to SvelteKit</h1>
	<p>
		Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation
	</p>

	<Counter />
	<Table />
</main>
