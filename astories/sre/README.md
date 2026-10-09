# sre — Site Reliability Engineering (vận hành cho đáng tin)

> **Mắt xích cuối** của mạch cloud: sau *hiểu* → *biết dịch vụ* → *thiết kế*, giờ là **vận hành cho đáng tin trong production**. Tổ chức **theo khái niệm SRE**, xây dần trên nền *error budget*.

## Bốn tầng — kim tự tháp

```
   sre          —  "giữ hệ SỐNG dưới áp lực thật"  (operate reliably)   ← bạn ở đây
   ─────────────────────────────────────────────────────────────
   aws-design   —  "làm sao cho đúng"  (design)
   aws-fund     —  "có dịch vụ gì"     (what)
   cloud-base   —  "vì sao nó thế"     (why)
```

## Danh sách bài (9 bài, 0–8)

| # | Bài | Trụ SRE |
| :-- | :-- | :-- |
| 0 | [SRE là gì + error budget](bai_hoc/bai_00_sre-la-gi-error-budget.md) | reliability là đánh đổi |
| 1 | [SLI / SLO / SLA](bai_hoc/bai_01_sli-slo-sla.md) | đo đúng, đặt mục tiêu |
| 2 | [Observability & golden signals](bai_hoc/bai_02_observability-golden-signals.md) | nhìn thấy hệ |
| 3 | [Alerting](bai_hoc/bai_03_alerting.md) | báo động theo triệu chứng |
| 4 | [Toil & automation](bai_hoc/bai_04_toil-automation.md) | diệt việc lặp tay |
| 5 | [Incident response & on-call](bai_hoc/bai_05_incident-oncall.md) | ứng cứu có kỷ luật |
| 6 | [Postmortem culture](bai_hoc/bai_06_postmortem.md) | học từ sự cố, blameless |
| 7 | [Quá tải & cascading failure](bai_hoc/bai_07_overload-cascading.md) | chịu tải, không sập dây chuyền |
| 8 | [Chaos engineering & testing](bai_hoc/bai_08_chaos-testing.md) | chủ động tiêm lỗi |

## Nguồn (Luật số 1)

| Mã | Nguồn | Trích |
| :-- | :-- | :-- |
| **SRE** | Google *Site Reliability Engineering* (bản online `sre.google/sre-book`) | `SRE: <chương>` → `tai_lieu/sre_*.txt` |
| **SREWB** | *The Site Reliability Workbook* (PDF) | `SREWB (tr. X)`, PDF = tr. + 32 |

## Phong cách

Giữ kiểu dễ hình dung của các khoá trước: mỗi bài mở bằng **tình huống cụ thể**, **ẩn dụ đời thường** cho khái niệm trừu tượng, và **ví dụ số dắt tay**; demo TS chạy thật/tất định; áp khái niệm lên **Notes API capstone** (aws-fund). Cross-link hai chiều với [`aws-design`](../aws-design/README.md), [`aws-fund`](../aws-fund/README.md), [`cloud-base`](../cloud-base/README.md).
