<script lang="ts">
	import * as Table from '$lib/components/ui/table';
	import Card from '$lib/components/ui/card/card.svelte';
	import { OpenAPI, DefaultService } from '$lib/api';
	import type { Order } from '$lib/api/models/Order';
	import { onMount } from 'svelte';

	let data: Order[] = [];

	onMount(async () => {
		OpenAPI.BASE = 'http://localhost:8000';
		data = await DefaultService.getOrders();
	});
</script>

<!-- Add a new line -->

<Card>
	<h1 class="mb-4 px-2 text-lg font-medium">Trade Table</h1>
	<Table.Root class="p-6">
		<Table.Header class="bg-slate-800/70">
			<Table.Row>
				<Table.Head>Order Id</Table.Head>
				<Table.Head>Side</Table.Head>
				<Table.Head>Size</Table.Head>
				<Table.Head>Price</Table.Head>
				<Table.Head>Timestamp</Table.Head>
				<Table.Head>Symbol</Table.Head>
				<Table.Head class="text-center">Status</Table.Head>
			</Table.Row>
		</Table.Header>

		<Table.Body>
			{#each data as parameter, i (parameter.id ?? i)}
				<Table.Row>
					<Table.Cell class="font-mono text-xs">{parameter.id}</Table.Cell>
					<Table.Cell>{parameter.side}</Table.Cell>
					<Table.Cell>{parameter.size}</Table.Cell>
					<Table.Cell>{parameter.price}</Table.Cell>
					<Table.Cell>{parameter.timestamp}</Table.Cell>
					<Table.Cell>{parameter.symbol}</Table.Cell>
					<Table.Cell>{parameter.status}</Table.Cell>
				</Table.Row>
			{/each}
		</Table.Body>
	</Table.Root>
</Card>
