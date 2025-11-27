/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */

/**
 * An order object for a trade.
 */
export type Order = {
	/**
	 * Unique identifier for the order
	 */
	id: string;
	/**
	 * Trading symbol (e.g., BTCUSD)
	 */
	symbol: string;
	/**
	 * Size of the order
	 */
	size: number;
	/**
	 * Price at which the order was placed
	 */
	price: number;
	/**
	 * Timestamp when the order was created
	 */
	timestamp: string;
	/**
	 * Exchange where the order was placed
	 */
	exchange: string;
	/**
	 * Side of the order (buy/sell)
	 */
	side: string;
	/**
	 * Current status of the order (e.g., open, closed, canceled)
	 */
	status: string;
};
