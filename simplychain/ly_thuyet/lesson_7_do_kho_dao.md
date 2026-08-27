# Độ khó đào (Mining Difficulty)

> Bài học dựa trên video **"Mining Difficulty – Simply Explained"** (kênh *Simply Explained – Savjee*, YouTube `o1gOyhU6XEw`).
> Đào sâu phần 6 của [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md), nơi Proof of Work mới chỉ được giới thiệu ở mức "tìm hash bắt đầu bằng N số 0".
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua — đọc để hiểu *tại sao*, không chỉ *cái gì*.

---

## Mục lục

1. [Vấn đề: giữ nhịp 10 phút khi hashrate đổi liên tục](#1-vấn-đề-giữ-nhịp-10-phút-khi-hashrate-đổi-liên-tục)
2. [Target — luật thật của Proof of Work](#2-target--luật-thật-của-proof-of-work)
3. [Điều chỉnh mỗi 2016 block](#3-điều-chỉnh-mỗi-2016-block)
4. [Giới hạn 4 lần](#4-giới-hạn-4-lần)
5. [Không có ai điều chỉnh cả](#5-không-có-ai-điều-chỉnh-cả)
6. [📚 nBits — nén số 256 bit vào 4 byte](#6--nbits--nén-số-256-bit-vào-4-byte)
7. [📚 "Difficulty" là gì về mặt toán học](#7--difficulty-là-gì-về-mặt-toán-học)
8. [📚 Hiểu nhầm lớn nhất: block KHÔNG đều 10 phút](#8--hiểu-nhầm-lớn-nhất-block-không-đều-10-phút)
9. [📚 Lỗi off-by-one có thật trong Bitcoin](#9--lỗi-off-by-one-có-thật-trong-bitcoin)
10. [📚 Timestamp và tấn công time-warp](#10--timestamp-và-tấn-công-time-warp)
11. [📚 Hashrate không đo được — nó được ước lượng](#11--hashrate-không-đo-được--nó-được-ước-lượng)
12. [📚 Mining pool và share difficulty](#12--mining-pool-và-share-difficulty)
13. [📚 Kinh tế học: halving, hash price, death spiral](#13--kinh-tế-học-halving-hash-price-death-spiral)
14. [📚 Các chuỗi khác điều chỉnh khác](#14--các-chuỗi-khác-điều-chỉnh-khác)
15. [Code minh hoạ](#15-code-minh-hoạ)
16. [Từ điển thuật ngữ](#16-từ-điển-thuật-ngữ)
17. [Câu hỏi tự kiểm tra](#17-câu-hỏi-tự-kiểm-tra)

---

## 1. Vấn đề: giữ nhịp 10 phút khi hashrate đổi liên tục

Satoshi muốn Bitcoin ra block **trung bình mỗi 10 phút**. Nhưng tổng sức mạnh đào của mạng (**hashrate**) thay đổi không ngừng:

```
2009: vài CPU             →  ~0,000005 TH/s
2011: GPU                 →  ~10 TH/s
2013: ASIC thế hệ đầu     →  ~1.000 TH/s
2026: ASIC 3nm            →  ~700.000.000 TH/s
```

Tăng **hàng nghìn tỷ lần** trong 17 năm.

Nếu độ khó cố định:

| Tình huống    | Hậu quả                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------- |
| Hashrate tăng | Block ra sau vài giây → toàn bộ 21 triệu BTC bị đào hết trong vài tháng → lịch phát hành sụp đổ |
| Hashrate giảm | Block ra sau vài ngày → mạng đóng băng, không ai giao dịch được                                 |

> **Giải pháp: độ khó phải TỰ ĐỘNG thích nghi.**

### Vì sao 10 phút

Đây là một **đánh đổi**, không phải con số thiêng ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md) đã nêu):

- **Quá ngắn** → block chưa kịp lan khắp mạng thì block tiếp theo đã xuất hiện → nhiều fork tạm thời, nhiều block mồ côi, lãng phí công đào.
- **Quá dài** → xác nhận giao dịch chậm, trải nghiệm tệ.

10 phút đủ để một block lan tới gần như mọi node trên toàn cầu trước khi block kế tiếp ra đời.

---

## 2. Target — luật thật của Proof of Work

[Bài 1](lesson_1_blockchain_hoat_dong_ntn.md) nói "tìm hash bắt đầu bằng N số 0". Đó là cách nói đơn giản hoá. Luật thật là:

```
   SHA-256( SHA-256( block_header ) )   <   TARGET
```

**`target`** là một số 256 bit. Hash của block — cũng là một số 256 bit — phải **nhỏ hơn** nó.

```
target LỚN  ──▶ nhiều hash thoả mãn ──▶ DỄ
target NHỎ  ──▶ ít hash thoả mãn   ──▶ KHÓ
```

### Vì sao "số 0 ở đầu" chỉ là hệ quả

Một số nhỏ, viết ở dạng hex 64 ký tự, **buộc phải** có nhiều số 0 ở đầu:

```
target = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
                                                                  ↑ difficulty 1
         └─ 8 số 0 ─┘

hash   = 0x00000000A1B2C3D4...  ✅ nhỏ hơn target → block HỢP LỆ
hash   = 0x0000000AFFFFFFFF...  ❌ lớn hơn target → thử nonce khác
```

> 💡 Nói "N số 0" là **gần đúng nhưng không chính xác**. Target di chuyển mượt mà, còn số lượng số 0 thì nhảy theo bậc. Mỗi số 0 hex thêm vào làm độ khó tăng **16 lần** — quá thô để điều chỉnh tinh vi. Bitcoin cần độ chi tiết mịn hơn, nên nó dùng phép so sánh số.

---

## 3. Điều chỉnh mỗi 2016 block

```
Cứ 2016 block một lần (khoảng 2 tuần), MỌI node tự tính lại target.
```

**Công thức:**

```
                            thời_gian_thực_tế_của_2016_block
   target_mới = target_cũ × ────────────────────────────────
                                1.209.600 giây (= 2 tuần)
```

### Đọc công thức này thế nào

| Thực tế                                 | Tỉ số | Target       | Độ khó           |
| --------------------------------------- | ----- | ------------ | ---------------- |
| 2016 block mất **1 tuần** (nhanh gấp 2) | 0,5   | Giảm một nửa | **Tăng gấp 2**   |
| 2016 block mất **2 tuần** (đúng nhịp)   | 1,0   | Không đổi    | Không đổi        |
| 2016 block mất **4 tuần** (chậm gấp 2)  | 2,0   | Tăng gấp đôi | **Giảm một nửa** |

> 💡 Chú ý **target và difficulty tỉ lệ NGHỊCH** với nhau. Target nhỏ đi = khó lên. Đây là chỗ hay nhầm nhất khi đọc tài liệu Bitcoin.

Đây là một **vòng phản hồi âm (negative feedback loop)** kinh điển — cùng loại cơ chế với bộ điều nhiệt trong tủ lạnh hay `base_fee` của EIP-1559 ([Bài 3](lesson_3_smart_contract.md)):

```
hashrate tăng ──▶ block ra nhanh ──▶ độ khó TĂNG ──▶ block chậm lại ──┐
      ▲                                                               │
      └───────────────────────────────────────────────────────────────┘
```

Hệ thống **tự tìm về điểm cân bằng**, không cần ai giám sát.

### Vì sao 2016 block

```
2016 block × 10 phút = 20.160 phút = 14 ngày = đúng 2 tuần
```

Lại là một đánh đổi:

- **Cửa sổ ngắn** → phản ứng nhanh với biến động hashrate, nhưng **nhiễu**: một chuỗi may mắn ngẫu nhiên sẽ bị hiểu nhầm thành "hashrate tăng" ([phần 8](#8--hiểu-nhầm-lớn-nhất-block-không-đều-10-phút) giải thích vì sao nhiễu này lớn hơn bạn tưởng).
- **Cửa sổ dài** → ổn định, nhưng phản ứng chậm. Hashrate sụp 50% thì mạng phải bò suốt 4 tuần mới chỉnh xong.

2016 block là điểm cân bằng Satoshi chọn.

---

## 4. Giới hạn 4 lần

Bitcoin **chặn** mức điều chỉnh trong một lần:

```
Tăng tối đa:  4 lần
Giảm tối đa:  1/4 lần
```

Nếu 2016 block mất **16 tuần** (hashrate sụp 87%), công thức sẽ đòi giảm độ khó 8 lần — nhưng nó **bị ép** xuống chỉ còn 4 lần. Phải chờ đợt điều chỉnh sau.

**Vì sao cần giới hạn:** đây là một **cầu chì an toàn**. Nó chặn kẻ tấn công thao túng timestamp để đẩy độ khó xuống mức vô lý chỉ trong một đợt ([phần 10](#10--timestamp-và-tấn-công-time-warp)).

> 🧪 [Phần 15](#15-code-minh-hoạ) có code cài đặt đúng công thức này, kèm giới hạn 4x, và chứng minh nó hoạt động.

---

## 5. Không có ai điều chỉnh cả

Đây là điểm video nhấn mạnh, và nó quan trọng hơn vẻ ngoài.

> **Không có máy chủ nào công bố độ khó mới. Không có uỷ ban nào bỏ phiếu.**

Mỗi node **tự tính**, từ dữ liệu **đã có sẵn trong chuỗi** mà nó đang giữ:

```
Node đọc timestamp của block #N và block #(N−2015) trong chuỗi của mình
        ↓
Tự áp công thức
        ↓
Ra target mới
        ↓
Vì MỌI node có CÙNG chuỗi → MỌI node ra CÙNG một target
```

Đây là **tính tất định** ở [Bài 3](lesson_3_smart_contract.md) áp dụng vào chính luật đồng thuận: đầu vào công khai + hàm công khai = kết quả giống nhau cho tất cả, không cần trao đổi gì thêm.

> 💡 Node nào tính ra target khác sẽ **từ chối** các block hợp lệ và tự tách khỏi mạng. Luật đồng thuận **tự thực thi**: sai luật thì bạn tự loại mình, không cần ai đuổi.

---

## 6. 📚 nBits — nén số 256 bit vào 4 byte

Block header chỉ có **80 byte** ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md), phần 2). Không đủ chỗ cho một target 32 byte. Bitcoin nén nó thành **4 byte** gọi là `nBits`:

```
   nBits = 0x1D00FFFF
            ├┘└────┘
            │   └── mantissa (3 byte): 0x00FFFF
            └────── exponent (1 byte): 0x1D = 29

   target = mantissa × 256^(exponent − 3)
          = 0x00FFFF × 256^26
          = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
```

Đây thực chất là **dấu phẩy động cơ số 256** — giống cách máy tính lưu số thực, nhưng thô sơ hơn.

**Đánh đổi:** không phải target nào cũng biểu diễn được chính xác. Target thật luôn bị **làm tròn xuống** về giá trị nBits gần nhất. Sai số này nhỏ đến mức không đáng kể.

> ⚠️ **Một chi tiết dễ sập bẫy khi tự cài đặt:** nếu byte đầu của mantissa ≥ `0x80`, nó sẽ bị hiểu là **số âm** (Bitcoin dùng biểu diễn có dấu ở đây). Phải chèn thêm một byte `0x00` vào trước và tăng exponent lên 1. Code ở [phần 15](#15-code-minh-hoạ) xử lý đúng chỗ này.

### 📚 Lý thuyết bổ sung: `nBits` nằm ở đâu — giải phẫu 80 byte header

Ta vừa nói `nBits` chiếm 4 byte. Bốn byte đó nằm trong một cấu trúc cố định, và đây là **toàn bộ thứ mà Proof of Work thật sự băm**:

```
   BLOCK HEADER — LUÔN LUÔN đúng 80 byte, không hơn không kém

   offset  dài   trường           nội dung
   ──────  ────  ───────────────  ──────────────────────────────────────
      0     4    version          luật nào đang áp dụng, cờ báo hiệu nâng cấp
      4    32    prevBlockHash    móc xích về khối trước  (Bài 1)
     36    32    merkleRoot       nén TOÀN BỘ giao dịch vào 32 byte
     68     4    timestamp        giây Unix                (phần 10)
     72     4    nBits            target nén               (phần 6, ngay trên)
     76     4    nonce            thứ thợ đào quay          (Bài 1 §6)
   ──────────────────────────────────────────────────────────────────────
     80 byte  ──sha256──▶ ──sha256──▶  hash của khối
```

Ba điều rút ra ngay từ bảng này:

1. **Đào chỉ băm 80 byte, không băm cả khối.** Khối có thể nặng 2 MB nhưng thợ đào chỉ quay đi quay lại 80 byte này. Toàn bộ giao dịch đã bị nén sẵn vào 32 byte `merkleRoot`.
2. **Chỉ có `nonce` là 4 byte** — tức chỉ ~4,3 tỷ khả năng, ít hơn hashrate mạng trong **một giây**. Nên thợ đào còn phải đổi cả `timestamp` và phần dữ liệu tự do trong giao dịch coinbase để có thêm không gian tìm kiếm.
3. **Đổi bất kỳ trường nào cũng phải đào lại từ đầu** — đây chính là "sửa một khối là hỏng cả đuôi" của [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md), nhìn ở mức byte.

#### Cái bẫy thứ tự byte

Bitcoin ghi mọi số theo **little-endian**, và hash thì lưu **ngược** với cách hiển thị trên trình duyệt chuỗi:

```
   Hash hiển thị :  000000000019d668...0a8ce26f
   Hash trong file:  6fe28c0a...68d6190000000000     <- đảo toàn bộ 32 byte
```

Đây là lỗi số một khi tự dựng giao dịch Bitcoin bằng tay: mọi thứ đúng hết, chỉ hash không khớp.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
/**
 * Bài 7 — bổ sung: 80 byte của một block header, dựng lại từ số 0.
 * Kiểm chứng bằng chính khối genesis của Bitcoin (03/01/2009).
 * Chạy: node demo.ts   (Node 22.6+, không cần cài gì)
 */
import { strict as assert } from "node:assert";
import { createHash } from "node:crypto";

/** Bitcoin băm HAI lần bằng SHA-256. */
const sha256d = (b: Buffer): Buffer =>
  createHash("sha256").update(createHash("sha256").update(b).digest()).digest();

/** Số nguyên 4 byte, little-endian — cách Bitcoin ghi mọi số trong header. */
const u32le = (n: number): Buffer => {
  const b = Buffer.alloc(4);
  b.writeUInt32LE(n >>> 0);
  return b;
};

/**
 * Hash hiển thị (trên explorer) là ĐẢO NGƯỢC của hash lưu trong header.
 * Đây là bẫy kinh điển khi tự dựng giao dịch Bitcoin.
 */
const displayToInternal = (hex: string): Buffer =>
  Buffer.from(hex, "hex").reverse();
const internalToDisplay = (buf: Buffer): string =>
  Buffer.from(buf).reverse().toString("hex");

interface BlockHeader {
  version: number;
  prevBlockHash: string; // dạng hiển thị
  merkleRoot: string; // dạng hiển thị
  timestamp: number; // giây Unix
  bits: number; // độ khó nén trong 4 byte
  nonce: number;
}

/** Ghép đúng 80 byte theo thứ tự Bitcoin quy định. */
function serializeHeader(h: BlockHeader): Buffer {
  const buf = Buffer.concat([
    u32le(h.version), //  4 byte
    displayToInternal(h.prevBlockHash), // 32 byte
    displayToInternal(h.merkleRoot), // 32 byte
    u32le(h.timestamp), //  4 byte
    u32le(h.bits), //  4 byte
    u32le(h.nonce), //  4 byte
  ]);
  assert.equal(buf.length, 80, "header Bitcoin LUÔN là 80 byte");
  return buf;
}

const blockHash = (h: BlockHeader): string =>
  internalToDisplay(sha256d(serializeHeader(h)));

/** nBits -> target. 1 byte mũ + 3 byte phần định trị. Xem lại phần nBits ở trên. */
function bitsToTarget(bits: number): bigint {
  const exponent = BigInt(bits >>> 24);
  const mantissa = BigInt(bits & 0x00ffffff);
  return mantissa * 2n ** (8n * (exponent - 3n));
}

/* ===========================================================================
 * 1. Dựng lại khối genesis của Bitcoin — 03/01/2009
 * ======================================================================== */
console.log("=== 1. Dung lai block header genesis cua Bitcoin ===");

const GENESIS: BlockHeader = {
  version: 1,
  prevBlockHash: "0".repeat(64), // khong co khoi truoc
  merkleRoot: "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
  timestamp: 1_231_006_505, // 2009-01-03 18:15:05 UTC
  bits: 0x1d00ffff,
  nonce: 2_083_236_893,
};

const raw = serializeHeader(GENESIS);
console.log(`  80 byte tho: ${raw.toString("hex")}\n`);

const layout: [string, number, number][] = [
  ["version      ", 0, 4],
  ["prevBlockHash", 4, 32],
  ["merkleRoot   ", 36, 32],
  ["timestamp    ", 68, 4],
  ["bits         ", 72, 4],
  ["nonce        ", 76, 4],
];
console.log("  truong          offset  dai            gia tri (hex, thu tu byte trong file)");
for (const [name, off, len] of layout) {
  const slice = raw.subarray(off, off + len).toString("hex");
  const short = slice.length > 24 ? slice.slice(0, 20) + "..." : slice;
  console.log(`  ${name}  ${String(off).padStart(4)}  ${String(len).padStart(3)} byte   ${short}`);
}

const hash = blockHash(GENESIS);
const EXPECTED = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f";
console.log(`\n  sha256(sha256(80 byte)) -> ${hash}`);
console.log(`  hash genesis that       -> ${EXPECTED}`);
console.log(`  KHOP: ${hash === EXPECTED}`);
assert.equal(hash, EXPECTED, "khong dung lai duoc genesis");

/* ===========================================================================
 * 2. Vì sao độ khó nằm sẵn trong header
 * ======================================================================== */
console.log("\n=== 2. bits -> target, va so 0 mo dau ===");
const target = bitsToTarget(GENESIS.bits);
console.log(`  bits   = 0x${GENESIS.bits.toString(16)}`);
console.log(`  target = ${target.toString(16).padStart(64, "0")}`);
console.log(`  hash   = ${hash}`);
console.log(`  hash < target ? ${BigInt("0x" + hash) < target}`);
console.log("  -> 8 so 0 mo dau khong phai quy uoc, no la HE QUA cua target nay.");
assert.ok(BigInt("0x" + hash) < target);

/* ===========================================================================
 * 3. Đổi một byte -> hash vỡ, và khối mất hiệu lực
 * ======================================================================== */
console.log("\n=== 3. Doi dung MOT truong ===");
for (const [label, mutated] of [
  ["nonce +1     ", { ...GENESIS, nonce: GENESIS.nonce + 1 }],
  ["timestamp +1 ", { ...GENESIS, timestamp: GENESIS.timestamp + 1 }],
  ["version 1->2 ", { ...GENESIS, version: 2 }],
] as [string, BlockHeader][]) {
  const h = blockHash(mutated);
  const stillValid = BigInt("0x" + h) < target;
  console.log(`  ${label} -> ${h.slice(0, 32)}...  hop le: ${stillValid}`);
}
console.log("\n  -> Doi bat ky truong nao cung phai DAO LAI tu dau.");
console.log("     Day chinh la ly do sua lich su ton kem — o muc byte.");

/* ===========================================================================
 * 4. Header KHÔNG chứa giao dịch — chỉ chứa gốc Merkle
 * ======================================================================== */
console.log("\n=== 4. 80 byte do KHONG he chua giao dich nao ===");
console.log("  Ca khoi co the nang 1-2 MB, nhung header luon dung 80 byte.");
console.log("  Giao dich duoc nen vao 32 byte merkleRoot.");
console.log("  -> Node nhe (SPV) chi tai chuoi header: 80 byte x chieu cao khoi.");
const heightNow = 900_000; // xap xi
const headersMb = (80 * heightNow) / 1_000_000;
console.log(`  ~${heightNow.toLocaleString("en-US")} khoi x 80 byte = ${headersMb.toFixed(1)} MB`);
console.log("  Do la toan bo thu can de kiem duoc Proof of Work cua ca chuoi.");

console.log("\nXong. 80 byte, 6 truong, va mot hash khop voi Bitcoin that.");
```

Kết quả chạy thật:

```
=== 1. Dung lai block header genesis cua Bitcoin ===
  80 byte tho: 0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c

  truong          offset  dai            gia tri (hex, thu tu byte trong file)
  version           0    4 byte   01000000
  prevBlockHash     4   32 byte   00000000000000000000...
  merkleRoot       36   32 byte   3ba3edfd7a7b12b27ac7...
  timestamp        68    4 byte   29ab5f49
  bits             72    4 byte   ffff001d
  nonce            76    4 byte   1dac2b7c

  sha256(sha256(80 byte)) -> 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
  hash genesis that       -> 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
  KHOP: true

=== 2. bits -> target, va so 0 mo dau ===
  bits   = 0x1d00ffff
  target = 00000000ffff0000000000000000000000000000000000000000000000000000
  hash   = 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
  hash < target ? true
  -> 8 so 0 mo dau khong phai quy uoc, no la HE QUA cua target nay.

=== 3. Doi dung MOT truong ===
  nonce +1      -> 9b227a4a5daa0cbae6874144bc5d7797...  hop le: false
  timestamp +1  -> 775212d740bc3900e6c050f43c2cb2db...  hop le: false
  version 1->2  -> dc3cdc644648f04c5b3c0266824f2420...  hop le: false

  -> Doi bat ky truong nao cung phai DAO LAI tu dau.
     Day chinh la ly do sua lich su ton kem — o muc byte.

=== 4. 80 byte do KHONG he chua giao dich nao ===
  Ca khoi co the nang 1-2 MB, nhung header luon dung 80 byte.
  Giao dich duoc nen vao 32 byte merkleRoot.
  -> Node nhe (SPV) chi tai chuoi header: 80 byte x chieu cao khoi.
  ~900,000 khoi x 80 byte = 72.0 MB
  Do la toan bo thu can de kiem duoc Proof of Work cua ca chuoi.

Xong. 80 byte, 6 truong, va mot hash khop voi Bitcoin that.
```

> 💥 **Đoạn code này dựng lại đúng hash khối genesis mà Satoshi tạo ngày 3/1/2009**, chỉ từ sáu con số và một hàm băm. Không có API, không có thư viện, không tải gì về. Đó là toàn bộ "phép màu" của Proof of Work ở mức byte.
>
> Con số **72 MB** ở cuối cũng đáng nhớ: đó là toàn bộ dung lượng cần để **tự kiểm chứng** Proof of Work của cả lịch sử Bitcoin. Node nhẹ (SPV) sống được là nhờ chính con số này — [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md) và [Bài 4](lesson_4_ung_dung_blockchain.md) phần bằng chứng Merkle.

---

## 7. 📚 "Difficulty" là gì về mặt toán học

Con số "difficulty" bạn thấy trên các trang thống kê **không** nằm trong block. Nó là một đại lượng dẫn xuất, cho dễ đọc:

```
                   target_của_difficulty_1
   difficulty = ─────────────────────────────
                     target_hiện_tại
```

Nói cách khác: **"khó gấp bao nhiêu lần so với thời genesis block"**.

### Xác suất và kỳ vọng

Mỗi phép hash là một lần bốc thăm độc lập:

```
   P(một hash trúng) = (target + 1) / 2²⁵⁶
```

Số phép hash kỳ vọng để tìm được một block:

```
   E[số hash] = 2²⁵⁶ / (target + 1) ≈ difficulty × 2³²
                                                    ↑
                                        ≈ 4,29 tỷ phép hash
```

Quy tắc bỏ túi:

> **Mỗi đơn vị difficulty ≈ 4,29 tỷ phép hash.**

| Difficulty       | Số hash kỳ vọng / block |
| ---------------- | ----------------------- |
| 1 (2009)         | 4,3 × 10⁹               |
| 1 triệu          | 4,3 × 10¹⁵              |
| 120.000 tỷ (nay) | **5,2 × 10²³**          |

> 💡 Con số cuối: mạng Bitcoin thực hiện khoảng **520 tỷ tỷ** phép hash cho **mỗi** block. Cứ 10 phút một lần. Suốt ngày đêm.

### Suy ra hashrate

```
   hashrate ≈ difficulty × 2³² / 600 giây
```

Đây là công thức mọi trang thống kê dùng — và nó chỉ là **ước lượng**, xem [phần 11](#11--hashrate-không-đo-được--nó-được-ước-lượng).

---

## 8. 📚 Hiểu nhầm lớn nhất: block KHÔNG đều 10 phút

Nếu bạn chỉ nhớ **một** điều từ bài này, hãy nhớ điều này.

> **Bitcoin KHÔNG ra block mỗi 10 phút. Nó ra block trung bình mỗi 10 phút. Hai câu đó khác nhau rất xa.**

### Đào là một quá trình Poisson

Mỗi phép hash là một phép thử độc lập với xác suất thành công cực nhỏ, lặp lại cực nhiều lần. Đây chính xác là định nghĩa của **quá trình Poisson**, và thời gian giữa hai sự kiện tuân theo **phân bố mũ (exponential distribution)**:

```
   P(block mất hơn t phút) = e^(−t/10)
```

**Bảng số thật** (khớp với mô phỏng 200.000 block ở [phần 15](#15-code-minh-hoạ)):

| Sự kiện                   | Xác suất  |
| ------------------------- | --------- |
| Block mất **hơn 10** phút | **36,8%** |
| Block mất **dưới 1** phút | **9,5%**  |
| Block mất **hơn 20** phút | 13,5%     |
| Block mất **hơn 30** phút | 5,0%      |
| Block mất **hơn 60** phút | 0,25%     |

Đọc lại hai dòng đầu:

- **Hơn một phần ba** số block mất **hơn** 10 phút.
- **Cứ 10 block thì có 1** ra trong vòng chưa đầy 1 phút.

### 📚 Tính chất "không nhớ" (memorylessness)

Phân bố mũ có một tính chất phản trực giác mà bạn nên nắm:

> **Đã 20 phút chưa có block nào. Thời gian chờ dự kiến cho block tiếp theo là bao lâu?**
>
> **Trả lời: 10 phút. Y như lúc đầu.**

Việc đã chờ 20 phút **không** làm block tới gần hơn. Mạng không "đến hẹn". Mỗi phép hash là một lần bốc thăm mới, hoàn toàn độc lập với mọi lần bốc trước.

Giống tung xu: đã ra 10 mặt ngửa liên tiếp thì lần thứ 11 vẫn là 50/50. Đây là lý do **"quy luật số nhỏ"** (gambler's fallacy) sai.

### Vì sao điều này quan trọng thực tế

| Hệ quả                                     | Giải thích                                                                                                                                         |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **"6 xác nhận ≈ 1 giờ" chỉ là trung bình** | Có thể mất 20 phút, có thể mất 3 tiếng. Cả hai đều bình thường.                                                                                    |
| **Nhiễu trong điều chỉnh độ khó**          | Một cửa sổ 2016 block có thể lệch vài phần trăm chỉ do **may rủi**, không phải do hashrate đổi. Đây là một lý do nữa để cửa sổ đủ dài.             |
| **Đào solo là xổ số**                      | Xem [phần 12](#12--mining-pool-và-share-difficulty).                                                                                               |
| **Phí tăng vọt khi block chậm**            | Một block trễ 40 phút làm mempool ùn lại, người dùng đua nhau trả phí cao. Bạn từng thấy phí Bitcoin nhảy vọt không lý do — thường chỉ là **xui**. |

---

## 9. 📚 Lỗi off-by-one có thật trong Bitcoin

Đây là một chi tiết vui và cũng dạy được nhiều điều.

Bitcoin điều chỉnh mỗi **2016 block**, và tính thời gian bằng cách lấy timestamp block cuối trừ timestamp block đầu của cửa sổ. Nhưng:

```
2016 block  →  chỉ có 2015 KHOẢNG giữa chúng
```

Kiểu như: 10 cái cột hàng rào tạo ra 9 khoảng trống, không phải 10.

Kết quả: mục tiêu thời gian thật của Bitcoin là

```
   1.209.600 / 2015 = 600,30 giây = 10,0050 phút
```

**không phải** 10,0000 phút.

### Hệ quả

Bitcoin chạy chậm hơn dự định khoảng **0,05%**. Nghe nhỏ, nhưng qua nhiều năm nó dồn lại: đợt halving tới đến muộn hơn vài ngày so với tính toán "10 phút chẵn".

**Vì sao không sửa?** Vì sửa luật đồng thuận là một **hard fork** ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md), phần 7): mọi node phải nâng cấp đồng thời, nếu không chuỗi tách đôi. Cho một lỗi vô hại 0,05% thì **không đáng**.

> 💡 **Bài học rộng hơn:** trong hệ thống đồng thuận, một **lỗi mà tất cả cùng mắc** thì không còn là lỗi — nó **trở thành đặc tả**. Sửa nó nguy hiểm hơn giữ nó. Đây là hiện tượng lặp lại khắp nơi trong Bitcoin (một ví dụ khác: lỗi off-by-one của opcode `OP_CHECKMULTISIG` khiến nó tiêu thêm một phần tử thừa trên stack — cũng không bao giờ được sửa).

---

## 10. 📚 Timestamp và tấn công time-warp

Công thức điều chỉnh dựa trên **timestamp do chính thợ đào khai báo**. Điều này mở ra một cửa tấn công.

### Luật kiểm tra timestamp

Bitcoin không thể tin timestamp, nên nó ràng buộc hai đầu:

| Luật                       | Nội dung                                                 |
| -------------------------- | -------------------------------------------------------- |
| **Median Time Past (MTP)** | Timestamp phải **lớn hơn** trung vị của 11 block trước   |
| **Luật 2 giờ**             | Timestamp không được vượt quá **thời gian mạng + 2 giờ** |

Giữa hai ràng buộc đó, thợ đào vẫn còn khá nhiều chỗ để lách.

### Time-warp attack

```
Kẻ tấn công kiểm soát phần lớn hashrate:
  ├─ Với hầu hết block: khai timestamp CHẬM nhất có thể (sát MTP)
  └─ Với block CUỐI của cửa sổ 2016: khai timestamp thật
        ↓
  Mạng tưởng 2016 block mất RẤT LÂU
        ↓
  Độ khó bị kéo XUỐNG
        ↓
  Lặp lại → độ khó rơi tự do → đào ra hàng loạt block gần như miễn phí
```

**Bitcoin chống được ở mức nào:**

- **Giới hạn 4x** ([phần 4](#4-giới-hạn-4-lần)) chặn không cho độ khó rơi quá nhanh trong một đợt.
- Cần **đa số hashrate** — mà nếu bạn đã có đa số hashrate thì bạn có nhiều cách tấn công đơn giản hơn.
- Luật MTP buộc timestamp phải tiến lên, không lùi tuỳ ý.

> ⚠️ Nhưng **các altcoin PoW nhỏ thì dính thật**. Verge (2018) bị time-warp kết hợp thao túng thuật toán đào, kẻ tấn công đào ra hàng triệu XVG. Bitcoin Cash phải bổ sung luật vá riêng. Bitcoin sống sót chủ yếu nhờ **hashrate quá lớn**, không phải nhờ công thức miễn nhiễm.

> 💡 Đây là chủ đề lặp lại: **cùng một thiết kế, an toàn ở quy mô lớn, mong manh ở quy mô nhỏ.** Bảo mật PoW **tỉ lệ thuận với hashrate**, nên chuỗi nhỏ hưởng ít bảo mật hơn dù dùng y hệt mã nguồn.

---

## 11. 📚 Hashrate không đo được — nó được ước lượng

Đây là điều gần như không ai nói ra.

> **Không tồn tại phép đo hashrate mạng.** Không máy chủ nào đếm. Thợ đào không báo cáo cho ai.

Con số bạn thấy trên các trang thống kê được **suy ngược** ra:

```
   hashrate ước lượng ≈ difficulty × 2³² / thời_gian_block_trung_bình
```

Nghĩa là: *"để tạo ra bấy nhiêu block ở độ khó này trong khoảng thời gian đó, mạng **hẳn phải** có chừng này hashrate."*

### Hệ quả

| Hệ quả                                 | Giải thích                                                                                                                                                                                             |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ước lượng rất nhiễu trong ngắn hạn** | Vì thời gian block phân bố mũ ([phần 8](#8--hiểu-nhầm-lớn-nhất-block-không-đều-10-phút)). Biểu đồ hashrate theo ngày dao động dữ dội — phần lớn là **nhiễu thống kê**, không phải thợ đào bật tắt máy. |
| **Cần cửa sổ dài mới có ý nghĩa**      | Trung bình động 7 ngày trở lên mới đáng tin.                                                                                                                                                           |
| **Không thể biết ai đang đào**         | Chỉ suy được **tổng**, không suy được thành phần.                                                                                                                                                      |

> 💡 Có một vẻ đẹp ở đây: Bitcoin đo lường **công sức toàn cầu** của mình bằng cách duy nhất mà một hệ phi tập trung có thể — **quan sát hệ quả, không quan sát nguyên nhân**. Không ai phải báo cáo gì cả; bằng chứng nằm trong chính các block.

---

## 12. 📚 Mining pool và share difficulty

### Đào solo là xổ số

Giả sử bạn có một dàn ASIC 100 TH/s trong mạng 700 EH/s:

```
Tỷ lệ hashrate của bạn : 0,0000143%
Kỳ vọng                : 0,0075 block/năm
                       → trung bình 133 NĂM cho một block
P(10 năm không được gì) : 92,8%
```

> 🧪 Số này được tính trong code ở [phần 15](#15-code-minh-hoạ).

Bạn hoặc trúng 3,125 BTC, hoặc **không được gì suốt cả đời**. Phương sai không thể chấp nhận được với một hoạt động kinh doanh phải trả tiền điện hàng tháng.

### Pool giải quyết thế nào: share

Pool tạo ra một **độ khó thấp hơn nhiều** cho riêng nội bộ:

```
Độ khó THẬT của mạng    : hash < target_mạng      (cực khó)
Độ khó SHARE của pool   : hash < target_pool      (dễ hơn hàng tỷ lần)
                                    ↑
                          thợ đào nộp "share" liên tục
                          → chứng minh mình ĐANG làm việc thật
```

Mỗi share là **bằng chứng công việc thu nhỏ**. Pool đếm share để chia thưởng công bằng. Và điểm mấu chốt:

> **Thỉnh thoảng, một share tình cờ cũng thoả mãn luôn target thật của mạng → pool tìm được block.**

Không có công sức nào bị lãng phí — cùng những phép hash đó vừa dùng để đếm công vừa dùng để săn block thật.

> 💡 Đây là một mẫu hình đẹp: **Proof of Work có thể phân cấp**. Cùng một cơ chế, chỉnh ngưỡng khó là dùng được cho một mục đích hoàn toàn khác (đo lường công sức thay vì chốt block). Cơ chế chống spam email Hashcash — thứ Satoshi lấy ý tưởng — chính là PoW ở một ngưỡng còn thấp hơn nữa.

### Cái giá: tập trung hoá

Pool giải quyết phương sai, nhưng tạo ra vấn đề đã nêu ở [Bài 5](lesson_5_proof_of_stake.md): vài pool kiểm soát phần lớn hashrate mạng.

**Nhưng có một sắc thái quan trọng:** pool kiểm soát **việc chọn giao dịch nào vào block**, còn hashrate thật thuộc về **hàng nghìn thợ đào riêng lẻ** có thể **chuyển pool trong vài phút**. Năm 2014, khi GHash.io chạm 51%, thợ đào tự nguyện rời đi và tỷ lệ tụt xuống — không cần ai can thiệp. Giao thức **Stratum V2** đẩy quyền chọn giao dịch về lại phía thợ đào, giảm hẳn rủi ro này.

---

## 13. 📚 Kinh tế học: halving, hash price, death spiral

### Halving va vào độ khó

Cứ 210.000 block (~4 năm), phần thưởng block **giảm một nửa**:

```
2009: 50 BTC  →  2012: 25  →  2016: 12,5  →  2020: 6,25  →  2024: 3,125
```

Nhưng **độ khó không tự giảm theo**. Sau halving:

```
Doanh thu thợ đào giảm 50% qua một đêm
        ↓
Thợ đào kém hiệu quả nhất lỗ → tắt máy ("miner capitulation")
        ↓
Hashrate giảm → block chậm lại
        ↓
Đợt điều chỉnh sau: độ khó GIẢM
        ↓
Số còn lại có lãi trở lại → cân bằng mới
```

**Hash price** — doanh thu trên mỗi TH/s mỗi ngày — là chỉ số mà thợ đào thực sự theo dõi. Nó gộp cả giá coin, độ khó và phí giao dịch vào một con số.

### "Death spiral" — vì sao nó chưa xảy ra

Lập luận của phe hoài nghi:

```
Giá giảm → thợ đào tắt máy → block chậm → mạng không dùng được
        → giá giảm tiếp → ... → Bitcoin chết
```

**Vì sao thực tế không diễn ra như vậy:**

| Lý do                                  | Giải thích                                                                                                                                                                                                                                                                                   |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Điều chỉnh độ khó chính là cầu chì** | Hashrate giảm thì độ khó giảm theo. Mạng **tự cân bằng lại** ở quy mô nhỏ hơn.                                                                                                                                                                                                               |
| **Thợ đào có chi phí rất khác nhau**   | Ai có điện rẻ vẫn lãi khi người khác đã lỗ. Không bao giờ tắt hết cùng lúc.                                                                                                                                                                                                                  |
| **Đã kiểm chứng thực tế**              | Tháng 6/2021 Trung Quốc cấm đào, hashrate Bitcoin **sụp hơn 50% trong vài tuần** — mức sụp lớn nhất lịch sử. Độ khó điều chỉnh giảm 28% (đợt giảm mạnh nhất từ trước tới nay), mạng chạy chậm vài tuần rồi **hồi phục hoàn toàn**. Không có block nào bị mất, không có giao dịch nào bị đảo. |

> 💡 Sự kiện 2021 là **bài kiểm tra thực địa tốt nhất** mà cơ chế điều chỉnh độ khó từng trải qua — và nó vượt qua. Một cơ chế viết năm 2008 đã xử lý được cú sốc mất một nửa mạng lưới mà không cần ai can thiệp.

### Độ khó chính là thước đo bảo mật

```
   Chi phí tấn công 51% ≈ chi phí sở hữu/thuê được hơn nửa hashrate hiện tại
```

Độ khó càng cao → hashrate càng lớn → viết lại lịch sử càng đắt. Nối thẳng vào [Bài 5](lesson_5_proof_of_stake.md): **PoW = bảo mật kiểu dòng chảy (flow)** — phải liên tục đốt tiền để duy trì, và cái giá đó chính là điều làm việc tấn công trở nên vô lý về mặt kinh tế.

---


### 📚 Lý thuyết bổ sung: mempool và thị trường phí

Xuyên suốt bài này ta nhắc tới phí mà chưa định nghĩa nơi nó được định giá. Đây là chỗ đó.

#### Mempool — và một hiểu nhầm ngay từ tên gọi

> ⚠️ **Không tồn tại "cái mempool" duy nhất.** Mỗi node giữ **mempool riêng của nó** — tập các giao dịch đã nghe thấy nhưng chưa vào block nào.

Các mempool **gần giống nhau nhưng không bao giờ y hệt**, vì mỗi node nghe thấy giao dịch ở thời điểm khác nhau và có chính sách lọc khác nhau. Website "mempool" bạn hay xem chỉ đang chiếu mempool của **một** node cụ thể.

```
Ví ký giao dịch  ──▶  phát tán P2P  ──▶  mempool của từng node
                                              │
                                    Thợ đào chọn từ mempool CỦA MÌNH
                                              │
                                    Xếp theo FEERATE giảm dần, nhồi đầy block
```

#### Phí tính theo KÍCH THƯỚC, không theo số tiền

Đây là điểm bất ngờ nhất với người mới:

```
   feerate = phí (satoshi) / kích thước (vByte)
```

Gửi 1 BTC hay 0,001 BTC — **phí như nhau** nếu giao dịch cùng kích thước. Thợ đào bán **chỗ trong block**, không bán dịch vụ chuyển tiền.

**vByte và weight unit** (nối vào SegWit ở [Bài 6](lesson_6_vi_bitcoin.md)):

```
weight = (dữ liệu KHÔNG phải witness) × 4  +  (dữ liệu witness) × 1
vByte  = weight / 4                         ← witness được chiết khấu 75%
Giới hạn block: 4.000.000 weight unit ≈ 1.000.000 vByte
```

> 💡 Đây chính là nguồn gốc con số "địa chỉ `bc1q` rẻ hơn ~16%" — chữ ký nằm ở vùng witness nên chỉ bị tính **một phần tư** trọng lượng.

Và nó giải thích lại điều đã nêu ở [phần 7 của Bài 6](lesson_6_vi_bitcoin.md#7--utxo--vì-sao-ví-không-có-số-dư): **phí phụ thuộc số UTXO bạn gộp**, vì mỗi input thêm vào là thêm ~68–148 vByte.

#### Vì sao phí nhảy vọt — nối thẳng vào phân bố Poisson

[Phần 8](#8--hiểu-nhầm-lớn-nhất-block-không-đều-10-phút) cho biết ~5% số block mất hơn 30 phút. Đây là hệ quả kinh tế của nó:

```
Giao dịch đến đều đặn ────▶ mempool
Block ra theo POISSON  ────▶ rút mempool THEO CỤM, không đều

Một block trễ 40 phút
   → mempool phình lên
   → ai cũng muốn vào block kế tiếp
   → đua nhau nâng feerate
   → phí tăng vọt trong vài chục phút rồi lắng xuống
```

> 💡 **Phần lớn các cú tăng phí ngắn hạn không có nguyên nhân nào cả — chỉ là xui.** Hàng đợi có tốc độ vào đều nhưng tốc độ ra ngẫu nhiên thì luôn dao động dữ dội. Đây là lý thuyết xếp hàng thuần tuý, không phải "thị trường hoảng loạn".

#### Khi trả phí hụt: hai lối thoát

| Cơ chế                            | Cách làm                                                                                                                              | Ai dùng được                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **RBF** (Replace-By-Fee, BIP-125) | Phát lại **chính giao dịch đó** với phí cao hơn, thay thế bản cũ trong mempool                                                        | **Người gửi** — phải bật cờ RBF từ đầu                     |
| **CPFP** (Child Pays For Parent)  | Tiêu output của giao dịch đang kẹt bằng một giao dịch con **phí rất cao**. Thợ đào muốn ăn phí con thì buộc phải đưa cả cha vào block | **Người nhận** cũng làm được — không cần người gửi hợp tác |

> 💡 CPFP hoạt động được vì thợ đào tối ưu theo **feerate của cả cụm (package)**, không theo từng giao dịch riêng lẻ. Đây cũng chính là lý do RBF gây tranh cãi: nó khiến giao dịch **chưa xác nhận** trở nên có thể thay thế, làm suy yếu tập quán chấp nhận thanh toán 0-conf.

#### Mempool đầy thì sao

Mempool có giới hạn bộ nhớ (mặc định 300 MB). Khi đầy, node **đuổi** các giao dịch feerate thấp nhất và nâng **mempool min fee** lên. Giao dịch bị đuổi không biến mất khỏi vũ trụ — nó chỉ bị quên, và phải được phát lại.

> ⚠️ Vì thế **"giao dịch của tôi kẹt vĩnh viễn"** hầu như không bao giờ đúng. Hoặc nó vào block, hoặc nó bị đuổi khỏi mempool và tiền chưa từng rời ví bạn. UTXO chỉ bị tiêu khi giao dịch **vào block**.

#### Vì sao ước lượng phí khó đến vậy

Ví phải đoán *"trả bao nhiêu để vào block trong N block tới"*. Bài toán này khó vì nó đòi dự báo **hai thứ ngẫu nhiên cùng lúc**:

1. Bao nhiêu giao dịch sẽ đến (không đoán được)
2. Bao nhiêu block sẽ ra trong khoảng đó — **phân bố Poisson**, phương sai bằng đúng kỳ vọng

> 💡 Toàn bộ bài học này khép lại ở đây: **độ khó giữ nhịp block ở mức trung bình 10 phút, nhưng nó không thể — và không nhằm — làm block ra đều.** Chính phương sai còn lại đó là thứ tạo ra thị trường phí.

---

## 14. 📚 Các chuỗi khác điều chỉnh khác

| Chuỗi                      | Cơ chế                            | Đặc điểm                                                        |
| -------------------------- | --------------------------------- | --------------------------------------------------------------- |
| **Bitcoin**                | Mỗi 2016 block, giới hạn 4x       | Ổn định, phản ứng chậm                                          |
| **Litecoin**               | Mỗi 2016 block, mục tiêu 2,5 phút | Giống Bitcoin, nhanh hơn 4 lần                                  |
| **Ethereum (trước Merge)** | Điều chỉnh **mỗi block**          | Phản ứng rất nhanh, mượt                                        |
| **Zcash, Dash…**           | **DigiShield / LWMA**             | Trung bình trượt cửa sổ ngắn                                    |
| **Monero**                 | Mỗi block, cửa sổ 720 block       | Chống thao túng timestamp tốt                                   |
| **Ethereum (sau Merge)**   | **Không có độ khó**               | PoS: slot 12 giây cố định ([Bài 5](lesson_5_proof_of_stake.md)) |

### Vì sao coin nhỏ cần thuật toán khác

Chuỗi nhỏ dễ dính **hash attack**: một dàn máy lớn nhảy vào đào vài giờ, ăn hết block dễ, rồi rút đi — để lại độ khó cao ngất và mạng đóng băng suốt nhiều ngày với những thợ đào còn lại.

**LWMA (Linearly Weighted Moving Average)** phản ứng trong vài block thay vì 2016, làm cuộc tấn công này không còn có lãi.

> 💡 Bitcoin không cần điều đó vì hashrate của nó **quá lớn để ai đó nhảy vào rồi rút ra** cho có ý nghĩa. Lại thêm một minh hoạ cho nhận xét ở [phần 10](#10--timestamp-và-tấn-công-time-warp): **quy mô bản thân nó là một tính năng bảo mật.**

### 📚 Difficulty bomb — một chương lịch sử

Ethereum từng nhúng một cơ chế cố ý: **difficulty bomb** (còn gọi *"kỷ băng hà"*) — độ khó tăng theo **hàm mũ** theo số block, bất kể hashrate.

Mục đích: **ép** cộng đồng phải chuyển sang PoS. Nếu ai đó muốn cố thủ ở PoW, chuỗi của họ sẽ dần đóng băng.

Quả bom bị **hoãn** nhiều lần (các đợt nâng cấp Byzantium, Constantinople, Muir Glacier, Arrow Glacier, Gray Glacier) cho đến khi The Merge hoàn tất năm 2022.

> 💡 Đây là một ví dụ hiếm hoi về **quản trị được mã hoá thẳng vào giao thức**: dùng chính luật kỹ thuật để tạo áp lực chính trị. Nối vào [Bài 3](lesson_3_smart_contract.md): dưới mọi lớp toán học, vẫn là **con người quản trị**.

---

## 15. Code minh hoạ

Cài đặt đúng công thức điều chỉnh của Bitcoin, kèm mã hoá nBits và mô phỏng phân bố thời gian block. Chỉ dùng thư viện chuẩn của Node.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
// difficulty.ts — Độ khó đào Bitcoin: nBits <-> target, công thức điều chỉnh, và
// phân bố THỜI GIAN BLOCK (thứ gây hiểu nhầm lớn nhất).
// Chạy: node difficulty.ts
import { strict as assert } from "node:assert";

const TWO256 = 1n << 256n;
const MAX_TARGET = 0x00FFFFn * 256n ** (0x1Dn - 3n);   // target của difficulty 1
const TARGET_TIMESPAN = 14 * 24 * 60 * 60;             // 2 tuần = 1.209.600 giây
const INTERVAL = 2016;                                  // số block mỗi lần điều chỉnh

/** Chia hai BigInt ra số thực — BigInt chia cụt nên phải scale trước. */
const ratio = (a: bigint, b: bigint, prec = 1_000_000n): number =>
  Number(a * prec / b) / Number(prec);

/** PRNG tất định (mulberry32) — thay cho random.seed() của Python. */
function seeded(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6D2B79F5) >>> 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ---------- nBits: nén target 256-bit vào 4 byte ----------
const bitsToTarget = (bits: number): bigint =>
  BigInt(bits & 0xFFFFFF) * 256n ** BigInt((bits >>> 24) - 3);

function targetToBits(target: bigint): number {
  let b = Buffer.from(target.toString(16).padStart(64, "0"), "hex");
  let i = 0;
  while (i < b.length && b[i] === 0) i++;
  b = b.subarray(i);
  if (b[0] > 0x7F) b = Buffer.concat([Buffer.from([0]), b]);  // bit đầu = 1 -> thêm byte 0
  const mant = Buffer.concat([b.subarray(0, 3), Buffer.alloc(3)]).subarray(0, 3);
  return (b.length << 24) | mant.readUIntBE(0, 3);
}

const difficulty = (target: bigint): number => ratio(MAX_TARGET, target);

function demoBits(): void {
  console.log("=== 1. nBits: 4 byte ma hoa mot so 256 bit ===");
  const genesisBits = 0x1D00FFFF;
  const t = bitsToTarget(genesisBits);
  console.log(`  nBits genesis : 0x${genesisBits.toString(16).padStart(8, "0")}`);
  console.log(`  -> target     : 0x${t.toString(16).padStart(64, "0")}`);
  console.log(`  -> so 0 dau   : ${(256 - t.toString(2).length) >> 2} chu so hex 0`);
  console.log(`  -> difficulty : ${difficulty(t).toLocaleString("en-US")}`);
  assert(t === MAX_TARGET && Math.abs(difficulty(t) - 1) < 1e-9);
  assert.equal(targetToBits(t), genesisBits);
  console.log("  ✓ round-trip nBits <-> target khop");
}

function demoExpectedHashes(): void {
  console.log("\n=== 2. Can bao nhieu phep hash? ===");
  for (const d of [1, 1e6, 1.2e14]) {
    const expHashes = d * 2 ** 32;                  // kỳ vọng = difficulty * 2^32
    console.log(`  difficulty ${d.toLocaleString("en-US").padStart(10)} -> ky vong ${expHashes.toExponential(3)} hash / block`);
  }
  // kiểm chứng: P(1 hash trúng) = (target+1)/2^256 -> E[hash] = 2^256/(target+1)
  const expHashesD1 = TWO256 / (MAX_TARGET + 1n);
  const r = Number(expHashesD1) / 2 ** 32;
  console.log(`  ✓ difficulty 1: 2^256/(target+1) = ${expHashesD1.toLocaleString("en-US")}`);
  console.log(`    2^32                           = ${(2 ** 32).toLocaleString("en-US")}   (ty le ${r.toFixed(6)})`);
  assert(Math.abs(r - 1) < 1e-4, "phai xap xi 2^32 (lech 0,0015% do 0xffff vs 0x10000)");
  console.log("  => 'difficulty' = so lan kho hon so voi difficulty 1");
}

/** Công thức điều chỉnh CHÍNH XÁC của Bitcoin, kể cả giới hạn 4x. */
function retarget(oldTarget: bigint, actualTimespan: number): [bigint, number] {
  const clamped = Math.max(TARGET_TIMESPAN / 4, Math.min(TARGET_TIMESPAN * 4, actualTimespan));
  const newTarget = oldTarget * BigInt(clamped) / BigInt(TARGET_TIMESPAN);
  return [newTarget < MAX_TARGET ? newTarget : MAX_TARGET, clamped];
}

function demoRetarget(): void {
  console.log("\n=== 3. DIEU CHINH DO KHO moi 2016 block ===");
  const d0 = 1e6;
  const t0 = MAX_TARGET / BigInt(d0);
  const cases: [string, number][] = [
    ["mang dao NHANH gap 2 (1 tuan)", TARGET_TIMESPAN / 2],
    ["mang dao dung 10 phut", TARGET_TIMESPAN],
    ["mang dao CHAM gap 2 (4 tuan)", TARGET_TIMESPAN * 2],
    ["hashrate SUP DO (16 tuan)", TARGET_TIMESPAN * 8],       // bị ép về 4x
  ];
  for (const [label, ts] of cases) {
    const [t1, clamped] = retarget(t0, ts);
    const note = clamped !== ts ? "  [BI EP 4x]" : "";
    console.log(`  ${label.padEnd(32)} -> difficulty ${Math.round(difficulty(t0)).toLocaleString("en-US")} -> ${Math.round(difficulty(t1)).toLocaleString("en-US")}${note}`);
  }
  assert(Math.abs(difficulty(retarget(t0, TARGET_TIMESPAN / 2)[0]) / d0 - 2) < 0.01, "nhanh gap 2 -> kho gap 2");
  assert(Math.abs(difficulty(retarget(t0, TARGET_TIMESPAN * 8)[0]) / d0 - 0.25) < 0.01, "phai bi ep xuong 1/4");
  console.log("  ✓ gioi han [1/4x .. 4x] hoat dong -> chan tan cong time-warp");
}

function demoOffByOne(): void {
  console.log("\n=== 4. LOI OFF-BY-ONE co that trong Bitcoin ===");
  // Bitcoin lấy timespan giữa block đầu và block CUỐI của cửa sổ 2016
  // -> đó là 2015 khoảng, không phải 2016!
  const realInterval = TARGET_TIMESPAN / (INTERVAL - 1);
  console.log(`  2016 block nhung chi co ${INTERVAL - 1} KHOANG giua chung`);
  console.log(`  -> muc tieu that = ${TARGET_TIMESPAN}/${INTERVAL - 1} = ${realInterval.toFixed(2)}s = ${(realInterval / 60).toFixed(4)} phut`);
  assert(Math.abs(realInterval / 60 - 10.0049) < 0.001);
  console.log("  => Bitcoin thuc te nham 10,0049 phut, KHONG phai 10,0000");
  console.log("  => Loi tu 2009, KHONG BAO GIO sua (sua = hard fork)");
}

function demoBlockTimeDistribution(): void {
  console.log("\n=== 5. HIEU NHAM LON NHAT: block KHONG deu 10 phut ===");
  const rnd = seeded(7);
  // Đào là QUÁ TRÌNH POISSON -> thời gian giữa các block phân bố MŨ
  const N = 200_000, mean = 10.0;
  const times = Array.from({ length: N }, () => -mean * Math.log(1 - rnd()));
  const avg = times.reduce((a, b) => a + b, 0) / N;
  console.log(`  mo phong ${N.toLocaleString("en-US")} block, trung binh = ${avg.toFixed(2)} phut`);
  assert(Math.abs(avg - mean) < 0.1);

  for (const thr of [1, 5, 10, 20, 30, 60]) {
    const emp = times.filter((t) => t > thr).length / N;
    const theo = Math.exp(-thr / mean);              // P(T > t) = e^(-t/mean)
    console.log(`    P(block > ${String(thr).padStart(2)} phut) = ${(emp * 100).toFixed(2).padStart(5)}%  (ly thuyet ${(theo * 100).toFixed(2).padStart(5)}%)`);
    assert(Math.abs(emp - theo) < 0.01);
  }
  const under1 = times.filter((t) => t < 1).length / N;
  console.log(`    P(block < 1 phut)  = ${(under1 * 100).toFixed(2).padStart(5)}%`);
  assert(under1 > 0.08 && under1 < 0.11);
  console.log("  => ~37% block cham hon 10 phut, ~10% nhanh hon 1 phut");
  console.log("  => 'Bitcoin ra block moi 10 phut' la noi ve TRUNG BINH, khong phai nhip dong ho");
}

function demoSoloMining(): void {
  console.log("\n=== 6. Vi sao khong ai dao mot minh nua ===");
  const netHashrate = 700e18;                         // ~700 EH/s
  const myHashrate = 100e12;                          // 1 dàn ASIC ~100 TH/s
  const share = myHashrate / netHashrate;
  const blocksPerYear = 6 * 24 * 365;
  const expected = share * blocksPerYear;
  const years = 1 / expected;
  console.log(`  ban chiem ${share.toExponential(3)} hashrate mang`);
  console.log(`  -> ky vong ${expected.toFixed(4)} block/nam  => trung binh ${Math.round(years).toLocaleString("en-US")} NAM/block`);
  const pNone10y = Math.exp(-expected * 10);
  console.log(`  -> P(10 nam khong duoc block nao) = ${(pNone10y * 100).toFixed(1)}%`);
  assert(years > 100 && pNone10y > 0.9);
  console.log("  => Do la ly do co MINING POOL: gop hashrate, chia thuong theo cong");
}

demoBits(); demoExpectedHashes(); demoRetarget();
demoOffByOne(); demoBlockTimeDistribution(); demoSoloMining();
console.log("\nAll assertions passed.");
```

**Kết quả chạy:**

```
=== 1. nBits: 4 byte ma hoa mot so 256 bit ===
  nBits genesis : 0x1d00ffff
  -> target     : 0x00000000ffff0000000000000000000000000000000000000000000000000000
  -> so 0 dau   : 8 chu so hex 0
  -> difficulty : 1
  ✓ round-trip nBits <-> target khop

=== 2. Can bao nhieu phep hash? ===
  difficulty          1 -> ky vong 4.295e+9 hash / block
  difficulty  1,000,000 -> ky vong 4.295e+15 hash / block
  difficulty 120,000,000,000,000 -> ky vong 5.154e+23 hash / block
  ✓ difficulty 1: 2^256/(target+1) = 4,295,032,833
    2^32                           = 4,294,967,296   (ty le 1.000015)
  => 'difficulty' = so lan kho hon so voi difficulty 1

=== 3. DIEU CHINH DO KHO moi 2016 block ===
  mang dao NHANH gap 2 (1 tuan)    -> difficulty 1,000,000 -> 2,000,000
  mang dao dung 10 phut            -> difficulty 1,000,000 -> 1,000,000
  mang dao CHAM gap 2 (4 tuan)     -> difficulty 1,000,000 -> 500,000
  hashrate SUP DO (16 tuan)        -> difficulty 1,000,000 -> 250,000  [BI EP 4x]
  ✓ gioi han [1/4x .. 4x] hoat dong -> chan tan cong time-warp

=== 4. LOI OFF-BY-ONE co that trong Bitcoin ===
  2016 block nhung chi co 2015 KHOANG giua chung
  -> muc tieu that = 1209600/2015 = 600.30s = 10.0050 phut
  => Bitcoin thuc te nham 10,0049 phut, KHONG phai 10,0000
  => Loi tu 2009, KHONG BAO GIO sua (sua = hard fork)

=== 5. HIEU NHAM LON NHAT: block KHONG deu 10 phut ===
  mo phong 200,000 block, trung binh = 9.99 phut
    P(block >  1 phut) = 90.39%  (ly thuyet 90.48%)
    P(block >  5 phut) = 60.57%  (ly thuyet 60.65%)
    P(block > 10 phut) = 36.69%  (ly thuyet 36.79%)
    P(block > 20 phut) = 13.52%  (ly thuyet 13.53%)
    P(block > 30 phut) =  5.04%  (ly thuyet  4.98%)
    P(block > 60 phut) =  0.25%  (ly thuyet  0.25%)
    P(block < 1 phut)  =  9.61%
  => ~37% block cham hon 10 phut, ~10% nhanh hon 1 phut
  => 'Bitcoin ra block moi 10 phut' la noi ve TRUNG BINH, khong phai nhip dong ho

=== 6. Vi sao khong ai dao mot minh nua ===
  ban chiem 1.429e-7 hashrate mang
  -> ky vong 0.0075 block/nam  => trung binh 133 NAM/block
  -> P(10 nam khong duoc block nao) = 92.8%
  => Do la ly do co MINING POOL: gop hashrate, chia thuong theo cong

All assertions passed.
```

**Sáu điều code này dạy:**

| Demo                | Bài học                                                                       |
| ------------------- | ----------------------------------------------------------------------------- |
| **1. nBits**        | 4 byte mã hoá được số 256 bit. Round-trip khớp → cài đặt đúng.                |
| **2. Kỳ vọng hash** | `difficulty × 2³²`. Mạng làm ~5,2 × 10²³ phép hash **cho mỗi block**.         |
| **3. Điều chỉnh**   | Nhanh gấp 2 → khó gấp 2. Giới hạn 4x chặn cú sốc và tấn công time-warp.       |
| **4. Off-by-one**   | Bitcoin thật sự nhắm 10,0049 phút. Lỗi trở thành đặc tả.                      |
| **5. Phân bố mũ**   | Mô phỏng khớp lý thuyết đến từng phần trăm: **36,8% block chậm hơn 10 phút**. |
| **6. Đào solo**     | 133 năm cho một block. Đây là lý do mining pool tồn tại.                      |

**Tự thử nghiệm:**

- Trong `demoBlockTimeDistribution`, tính **độ lệch chuẩn** của `times`. Với phân bố mũ, độ lệch chuẩn **bằng đúng** trung bình (10 phút) — đó là mức phương sai cực lớn, và giải thích vì sao thời gian block khó dự đoán đến vậy.
- Mô phỏng một cửa sổ 2016 block với hashrate **không đổi**, tính tổng thời gian, rồi chạy `retarget()`. Bạn sẽ thấy độ khó vẫn nhích lên xuống vài phần trăm — **thuần tuý do ngẫu nhiên**. Đó chính là nhiễu nói ở [phần 11](#11--hashrate-không-đo-được--nó-được-ước-lượng).
- Đặt `share = 0.51` trong `demoSoloMining` và tính lại kỳ vọng — bạn vừa mô hình hoá một kẻ tấn công 51%.
- Thử `targetToBits` với một target có byte đầu ≥ `0x80` để thấy quy tắc chèn byte `0x00` hoạt động.

---

## 16. Từ điển thuật ngữ

| Thuật ngữ                    | Giải thích                                               |
| ---------------------------- | -------------------------------------------------------- |
| **Hashrate**                 | Tổng số phép hash mạng thực hiện mỗi giây                |
| **Target**                   | Ngưỡng 256 bit; hash block phải nhỏ hơn nó               |
| **nBits**                    | Dạng nén 4 byte của target, nằm trong block header       |
| **Mantissa / Exponent**      | Hai phần của nBits — dấu phẩy động cơ số 256             |
| **Difficulty**               | `target_difficulty_1 / target_hiện_tại`                  |
| **Difficulty 1 target**      | `0x00000000FFFF0000...` — mốc so sánh gốc                |
| **Retarget**                 | Đợt điều chỉnh độ khó, mỗi 2016 block                    |
| **Target timespan**          | 1.209.600 giây = 2 tuần                                  |
| **Clamp 4x**                 | Giới hạn điều chỉnh trong [1/4x .. 4x] mỗi đợt           |
| **Negative feedback loop**   | Vòng phản hồi âm giữ hệ thống ở điểm cân bằng            |
| **Poisson process**          | Quá trình các sự kiện độc lập, tỷ lệ không đổi           |
| **Exponential distribution** | Phân bố thời gian giữa hai sự kiện Poisson               |
| **Memorylessness**           | Đã chờ bao lâu không ảnh hưởng thời gian chờ còn lại     |
| **MTP (Median Time Past)**   | Trung vị timestamp 11 block trước — chặn dưới            |
| **Luật 2 giờ**               | Timestamp không vượt quá giờ mạng + 2 tiếng              |
| **Time-warp attack**         | Thao túng timestamp để kéo độ khó xuống                  |
| **Share**                    | PoW ở độ khó thấp, dùng để đo công trong pool            |
| **Mining pool**              | Gộp hashrate, chia thưởng theo share                     |
| **Stratum V2**               | Giao thức trả quyền chọn giao dịch về cho thợ đào        |
| **Halving**                  | Phần thưởng block giảm nửa mỗi 210.000 block             |
| **Hash price**               | Doanh thu trên mỗi TH/s mỗi ngày                         |
| **Miner capitulation**       | Thợ đào lỗ đồng loạt tắt máy                             |
| **Death spiral**             | Kịch bản giá giảm → thợ đào bỏ → mạng chết (chưa xảy ra) |
| **Orphan / stale block**     | Block hợp lệ nhưng thua nhánh khác                       |
| **DigiShield / LWMA**        | Thuật toán điều chỉnh nhanh cho chuỗi nhỏ                |
| **Difficulty bomb**          | Cơ chế Ethereum cố ý tăng độ khó theo hàm mũ             |
| **ASIC**                     | Chip chuyên dụng chỉ để đào                              |

---

## 17. Câu hỏi tự kiểm tra

1. Chuyện gì xảy ra với Bitcoin nếu độ khó cố định và hashrate tăng 1000 lần?
2. Viết luật thật của Proof of Work. Vì sao "N số 0 ở đầu" chỉ là gần đúng?
3. Target và difficulty tỉ lệ thuận hay nghịch? Giải thích.
4. Viết công thức điều chỉnh độ khó. 2016 block mất 1 tuần thì độ khó thay đổi ra sao?
5. Vì sao có giới hạn 4x? Nó chặn tấn công gì?
6. Ai công bố độ khó mới? Trả lời rồi giải thích vì sao mọi node đồng ý với nhau.
7. nBits nén số 256 bit vào 4 byte bằng cách nào? Cái bẫy khi mantissa ≥ 0x80 là gì?
8. Một đơn vị difficulty tương ứng khoảng bao nhiêu phép hash?
9. **Xác suất một block Bitcoin mất hơn 10 phút là bao nhiêu?** Vì sao câu trả lời gây bất ngờ?
10. Đã 20 phút chưa có block. Thời gian chờ dự kiến còn lại là bao lâu? Tính chất này tên là gì?
11. Vì sao Bitcoin thực tế nhắm 10,0049 phút chứ không phải 10 phút chẵn?
12. Vì sao lỗi off-by-one đó không bao giờ được sửa? Bài học rộng hơn là gì?
13. Mô tả tấn công time-warp. Vì sao Bitcoin sống sót còn Verge thì không?
14. Hashrate mạng được **đo** hay được **ước lượng**? Bằng công thức nào? Hệ quả là gì?
15. Vì sao biểu đồ hashrate theo ngày dao động dữ dội?
16. Với 100 TH/s trong mạng 700 EH/s, trung bình bao lâu bạn đào được một block?
17. "Share" của mining pool là gì? Vì sao không có công sức nào bị lãng phí?
18. Pool kiểm soát cái gì, và **không** kiểm soát cái gì? Stratum V2 sửa gì?
19. Mô tả chuỗi sự kiện sau một đợt halving.
20. Vì sao "death spiral" chưa xảy ra? Nêu bằng chứng thực tế.
21. Vì sao coin nhỏ cần LWMA còn Bitcoin thì không?
22. Difficulty bomb của Ethereum dùng để làm gì? Nó nói lên điều gì về quản trị?

---

## Tóm tắt một trang

```
VẤN ĐỀ: hashrate tăng hàng NGHÌN TỶ lần trong 17 năm
        → độ khó phải TỰ ĐỘNG thích nghi để giữ nhịp ~10 phút

LUẬT THẬT:  SHA256(SHA256(header)) < TARGET
   target NHỎ = KHÓ  (target và difficulty TỈ LỆ NGHỊCH)
   "N số 0 ở đầu" chỉ là HỆ QUẢ, không phải luật

ĐIỀU CHỈNH mỗi 2016 block (~2 tuần):
   target_mới = target_cũ × (thời_gian_thực_tế / 2 tuần)
   nhanh gấp 2 → khó gấp 2 | giới hạn [1/4x .. 4x] = cầu chì chống time-warp
   KHÔNG AI công bố — mọi node TỰ TÍNH từ chuỗi mình có (tính tất định)

nBits: 4 byte = dấu phẩy động cơ số 256 (mantissa + exponent)
difficulty = target_d1 / target_hiện_tại
E[số hash/block] = difficulty × 2³² ≈ 5,2 × 10²³ ngày nay

⚠️ HIỂU NHẦM LỚN NHẤT: BLOCK KHÔNG ĐỀU 10 PHÚT
   Đào = QUÁ TRÌNH POISSON → thời gian block phân bố MŨ
   P(> 10 phút) = 36,8%   P(< 1 phút) = 9,5%   P(> 30 phút) = 5%
   TÍNH KHÔNG NHỚ: đã chờ 20 phút → vẫn còn kỳ vọng 10 phút nữa
   → 6 xác nhận "1 giờ" chỉ là trung bình; phí nhảy vọt thường chỉ là XUI

LỖI OFF-BY-ONE: 2016 block = 2015 KHOẢNG
   → Bitcoin thật sự nhắm 10,0049 phút. Không bao giờ sửa (= hard fork)
   → Lỗi mà TẤT CẢ cùng mắc thì trở thành ĐẶC TẢ

HASHRATE KHÔNG ĐO ĐƯỢC — chỉ SUY NGƯỢC từ difficulty & thời gian block
   → biểu đồ ngày dao động mạnh phần lớn là NHIỄU THỐNG KÊ

MINING POOL: solo = 133 NĂM/block → phương sai không chịu nổi
   SHARE = PoW ở ngưỡng thấp, đo công mà KHÔNG lãng phí hash nào
   Pool kiểm soát CHỌN GIAO DỊCH, không sở hữu hashrate (Stratum V2 trả lại quyền)

KINH TẾ: halving → doanh thu -50% → thợ yếu tắt máy → độ khó GIẢM → cân bằng lại
   "Death spiral" chưa xảy ra: điều chỉnh độ khó CHÍNH LÀ cầu chì
   Bằng chứng: TQ cấm đào 2021, hashrate sụp >50%, độ khó -28%, mạng HỒI PHỤC HOÀN TOÀN
   Độ khó = THƯỚC ĐO BẢO MẬT (PoW = bảo mật kiểu dòng chảy)

QUY MÔ TỰ NÓ LÀ TÍNH NĂNG BẢO MẬT — cùng mã nguồn, coin nhỏ dính time-warp/hash attack
```

---

**Nguồn:**
- Video gốc: [Mining Difficulty – Simply Explained](https://www.youtube.com/watch?v=o1gOyhU6XEw) (Simply Explained – Savjee)
- Satoshi Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008) — mục 4 & 11 (phân tích xác suất)
- Bitcoin Core, `pow.cpp` — `GetNextWorkRequired()` và `CalculateNextWorkRequired()`
- Andreas Antonopoulos, *Mastering Bitcoin* — chương 10 (Mining and Consensus)
- BIP-113 — *Median time-past as endpoint for lock-time calculations*

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. [Bài 4 – Ứng dụng blockchain](lesson_4_ung_dung_blockchain.md) — use case + khung quyết định *có cần blockchain không*
5. [Bài 5 – Proof of Stake](lesson_5_proof_of_stake.md) — staking, slashing, The Merge, Ouroboros, kho bạc on-chain
6. [Bài 6 – Ví Bitcoin](lesson_6_vi_bitcoin.md) — private key → địa chỉ, UTXO, seed phrase
7. **Bài 7 – Độ khó đào** ← *bạn đang ở đây* — target, nBits, retarget, phân bố Poisson
8. [Bài 8 – Zero-Knowledge Proof](lesson_8_zero_knowledge_proof.md) — sigma protocol, Fiat-Shamir, SNARK/STARK

*Phần mở rộng — nhìn từ trên xuống:*

9. [Bài 9 – Tiền mã hoá: toàn cảnh (và mặt tối)](../mo_rong/lesson_9_tien_ma_hoa_toan_canh.md) — tiền, lưu ký, stablecoin, lừa đảo, pháp lý
10. [Bài 10 – DeFi: tài chính phi tập trung](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md) — AMM, cho vay, flash loan, NFT, DAO
11. [Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning](../mo_rong/lesson_11_fork_va_lightning.md) — fork, kênh thanh toán, HTLC, thanh khoản
12. [Bài 12 – ERC-20: chuẩn token](../mo_rong/lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](../mo_rong/lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
