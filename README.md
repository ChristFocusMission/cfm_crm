# Christ Focus Mission — Fundraising Leads & Donor Stewardship Tracker

A web-based Fundraising Pipeline & Donor Relationship Management system built specifically for **Christ Focus Mission**, linked with **Google Firebase Cloud Firestore** for real-time collaboration across ministry team members and field fundraisers.

---

## 🌟 Key Features

1. **Pipeline Kanban Board**:
   - Visual stage workflow: `New / Identified` &rarr; `Contacted` &rarr; `Meeting / Pitch` &rarr; `Proposal Sent` &rarr; `Committed Partner 🎉` &rarr; `Deferred / Follow-up` &rarr; `Declined`.
   - Smooth drag-and-drop between stages.
   - Confetti celebration upon moving a partner to "Committed"!

2. **Dual Mode Architecture (Firebase + Local Storage)**:
   - **Live Firebase Cloud Firestore**: Real-time multi-user syncing via Firestore collections (`cfm_leads`, `cfm_campaigns`).
   - **Local / Demo Mode**: Full out-of-the-box functionality with LocalStorage and pre-seeded sample data. No initial setup required to test.
   - **In-App Firebase Config Modal**: Paste your Firebase credentials directly into the UI without touching code.
   - **One-Click Cloud Sync**: "Push Local Data to Firestore" button to immediately upload existing or custom leads to your live database.

3. **Rapid 5-Level Network Scaling Model**:
   - Proposed growth mechanism: Each member engages 10 members.
   - Milestone Target: 1,00,000 unique members (capped at Stage 5).
   - **Model A (One-Time Contribution)**: ₹1,000 / member &rarr; **₹10,00,00,000 (10 Crore)** gross.
   - **Model B (Monthly Subscription)**: ₹1,000 / month &rarr; **₹10,00,00,000 / month (10 Crore/mo)**, **₹1,20,00,00,000 / year (120 Crore Annualized Run-Rate)**.
   - Reconciled 5-Stage Tiers:
     - *Stage 1: Core Leaders* (10 members)
     - *Stage 2: Team Champions* (100 members)
     - *Stage 3: Active Distributors* (1,000 members)
     - *Stage 4: Brand Ambassadors & Builders* (10,000 members)
     - *Stage 5 (Capped): Active Supporters* (88,890 members, bringing total to 1,00,000)
   - Real-time activation simulator (10% to 100%) and CRM lead tier mapping.

4. **Pastoral Touchpoints & Prayer Intercession**:
   - Track personal and pastoral prayer requests for ministry partners.
   - Spiritual context callouts before reaching out to donors.
   - Interactive touchpoint timeline (log phone calls, meetings, emails, and prayer sessions).

4. **Mission Campaigns & Strategic Funds**:
   - Track targets vs. raised pledges for each campaign:
     - *General Mission & Operations Fund*
     - *Rural Church Planting Initiative*
     - *Youth & Discipleship Camp*
     - *Community Medical & Relief Outreach*
     - *Mission Training Center Expansion*
   - Real-time progress bars and pipeline breakdown per fund.

5. **Follow-ups & Overdue Alert System**:
   - Intelligent reminders for calls and meetings categorized by: *Overdue (Red Alert)*, *Due Today (Amber)*, and *Upcoming Scheduled*.

6. **Financial Reports & Analytics**:
   - Pipeline potential vs. confirmed received pledges.
   - Weighted probability forecast based on lead stages.
   - Multi-currency toggle: **USD ($)**, **INR (₹)**, **GBP (£)**, **EUR (€)**.
   - Instant export to CSV spreadsheet.

---

## 🚀 Running the Website Locally

You can launch the website locally with zero dependencies using Python 3:

```bash
cd /Users/jenishtilak/.gemini/antigravity/scratch/christ-focus-mission-fundraising
python3 server.py
```

Open your browser and navigate to:
```
http://localhost:8080
```
*(If port 8080 is in use, `server.py` will automatically choose an open port such as 8000 or 5000 and print the active URL in your terminal).*

---

## 🔥 Linking with Google Firebase

To connect the application to your live Firebase Cloud Firestore database:

### Step 1: Create a Firebase Project
1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click **Add project** and name it (e.g. `christ-focus-mission`).
3. Follow the prompts to create the project.

### Step 2: Enable Cloud Firestore
1. In the Firebase console left navigation, click **Build** &rarr; **Firestore Database**.
2. Click **Create database**.
3. Choose your database location and select **Start in test mode** (which allows initial read/write access), then click **Enable**.

### Step 3: Get Your Web App Configuration
1. In the Firebase console, click the **Project Settings** (gear icon next to Project Overview).
2. Under the **General** tab, scroll down to **Your apps** and click the Web icon (`</>`).
3. Register the app name (e.g. `CFM Fundraising Portal`).
4. Copy the `firebaseConfig` snippet. It will look like this:
   ```javascript
   const firebaseConfig = {
     apiKey: "AIzaSy...",
     authDomain: "christ-focus-mission.firebaseapp.com",
     projectId: "christ-focus-mission",
     storageBucket: "christ-focus-mission.appspot.com",
     messagingSenderId: "1234567890",
     appId: "1:1234567890:web:abcdef123456"
   };
   ```

### Step 4: Link in the Website
1. Open the website at `http://localhost:8080`.
2. Click the **Firebase Link** button in the top right navbar.
3. Paste the entire snippet into the **Quick Paste** box (or fill in the fields individually).
4. Click **Test Connection** to verify connectivity.
5. Click **Save & Connect**.
6. The status pill in the top header will turn green: `🟢 Firebase: christ-focus-mission`.
7. Click **Push Local Data to Firestore** to instantly populate your cloud database with the initial leads and campaigns!

---

## ☁️ Deploying to Firebase Hosting (Free)

To deploy this website so your entire team can access it online anywhere:

1. Install the Firebase CLI (if not already installed):
   ```bash
   npm install -g firebase-tools
   ```

2. Login to your Google account:
   ```bash
   firebase login
   ```

3. Initialize project (or link existing):
   ```bash
   firebase use --add <your-project-id>
   ```

4. Deploy with one command:
   ```bash
   firebase deploy
   ```

Firebase will output your live URL:
```
✔ Deploy complete!
Hosting URL: https://christ-focus-mission.web.app
```

---

## 🗄️ Firestore Database Schema

### Collection: `cfm_leads`
```json
{
  "name": "Dr. Arthur & Grace Vance",
  "organization": "Grace Family Healthcare",
  "leadType": "Major Donor",
  "email": "arthur.vance@gracehealth.org",
  "phone": "+1 (555) 349-8120",
  "city": "Dallas",
  "country": "USA",
  "preferredContact": "Phone",
  "stage": "committed",
  "expectedAmount": 15000,
  "receivedAmount": 15000,
  "currency": "USD",
  "frequency": "Annual",
  "campaignId": "camp-4",
  "priority": "High",
  "assignedTo": "Pastor David",
  "probability": 100,
  "nextFollowUp": "2026-11-15",
  "lastContactDate": "2026-10-10",
  "prayerRequests": "Pray for Grace's upcoming eye surgery and their son entering seminary.",
  "notes": "Committed $15,000 for Community Medical Outreach.",
  "activities": [
    {
      "id": "act-1",
      "date": "2026-10-10",
      "type": "Meeting",
      "summary": "In-person lunch with Pastor David. Received pledge check.",
      "author": "Pastor David"
    }
  ],
  "createdAt": "2026-09-01T10:00:00Z",
  "updatedAt": "2026-10-10T12:00:00Z"
}
```

### Collection: `cfm_campaigns`
```json
{
  "name": "Rural Church Planting Initiative",
  "code": "PLANT-2026",
  "target": 75000,
  "raised": 42000,
  "description": "Equipping local pastors and funding 12 new church plants in unreached rural districts.",
  "color": "blue"
}
```

---

## 📁 Project File Structure

```
christ-focus-mission-fundraising/
├── index.html              # Main Single-Page Application (Kanban, Table, Modals)
├── css/
│   └── styles.css          # Custom styling, animations, Kanban card layout
├── js/
│   ├── app.js              # Application logic, filters, reactive UI, drag-and-drop
│   ├── firebase-config.js  # Firebase SDK connection, Firestore sync & local fallback
│   └── sample-data.js      # Realistic seed data for Christ Focus Mission
├── server.py               # Lightweight local Python web server
├── firebase.json           # Firebase Hosting configuration
├── firestore.rules         # Cloud Firestore security rules
├── firestore.indexes.json  # Database compound indexes
└── README.md               # Documentation & setup guide
```
