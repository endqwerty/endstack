import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizeSku } from '../src/lib/sku.js';
test('normalizeSku trims and uppercases', () => { assert.equal(normalizeSku(' ab '), 'AB'); });
